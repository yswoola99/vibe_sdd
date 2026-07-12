# 구현 계획서: 오늘의 할 일 웹 앱

**브랜치**: `001-todo-web-app` | **작성일**: 2026-07-12 | **명세서**: [spec.md](spec.md)

**입력**: /specs/001-todo-web-app/spec.md

## 요약

이 기능은 단일 사용자용 할 일 관리 웹 앱으로, FastAPI 백엔드와 단일 HTML 프런트엔드를 사용해 할 일 생성/완료 토글/삭제/필터/남은 개수 표시 및 데이터 영속성을 제공한다. 구현은 REST API와 페이지 새로고침 없이 fetch 기반으로 동작하는 UI로 구성한다.

## 기술 컨텍스트

**언어/버전**: Python 3.11+

**주요 의존성**: FastAPI, SQLAlchemy 2.x, Pydantic, Jinja2, pytest, httpx/FastAPI TestClient

**저장소**: SQLite, 데이터베이스 경로는 .env의 DATABASE_URL 환경변수로 관리

**테스트**: pytest + FastAPI TestClient

**대상 플랫폼**: 웹 브라우저 기반

**프로젝트 유형**: 웹 애플리케이션

**성능 목표**: 단일 사용자, 소규모 데이터셋 기준으로 즉시 반응하는 수준

**제약 조건**: 별도 빌드 도구 없이 단일 index.html 기반 UI, 로컬 저장소 우선의 간단한 영속성

**규모/범위**: 기본 할 일 CRUD, 상태 필터, 남은 개수, 모바일 반응형 화면, API 테스트 포함

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- 모든 생성 문서(명세서, 계획서, 태스크, 체크리스트, 분석 리포트)는 한국어로 작성해야 한다.
- 스펙 우선 원칙에 따라 구현 전 스펙 범위를 확인하고, 테스트 필수 원칙에 따라 핵심 기능 테스트를 포함해야 한다.
- 환경설정은 .env/.env.example 기준으로 관리하고, 커밋 메시지는 태스크 ID를 포함해야 한다.

결과: 해당 원칙을 준수하는 방식으로 설계한다.

## 프로젝트 구조

### 문서(이 기능)

```text
specs/001-todo-web-app/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### 소스 코드(저장소 루트)

```text
app/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── database.py
└── templates/
    └── index.html

tests/
└── test_api.py
```

**구조 결정**: 단일 프로젝트 구조로 FastAPI 앱과 단일 HTML 템플릿을 함께 두며, API와 UI 로직은 app/ 아래에 배치한다.

## 복잡도 추적

해당 기능은 Constitution 기준을 위반하지 않으므로 별도 예외 없이 진행한다.
