"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

# 1. 소스 코드가 있는 루트 디렉토리 스캔 (Flat Layout 기준)
# "exclude" 패턴을 사용하여 문서화하지 않을 파일들을 뺍니다.
for path in sorted(Path(".").rglob("*.py")):
    # 제외할 파일/폴더 목록 (가상환경, 빌드폴더, 테스트폴더 등)
    if any(
        part.startswith(".") or part in {"tests", "build", "dist", "site"}
        for part in path.parts
    ):
        continue

    # 문서 생성 스크립트 자신도 제외
    if path.name == "gen_ref_pages.py":
        continue

    module_path = path.relative_to(".").with_suffix("")
    doc_path = path.relative_to(".").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    # 네비게이션(메뉴)에 추가
    nav[parts] = doc_path.as_posix()

    # 마크다운 파일 생성 (메모리 상에서)
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

# 네비게이션 파일 생성
with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
