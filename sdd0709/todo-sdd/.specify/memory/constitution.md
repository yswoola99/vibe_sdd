<!--
Sync Impact Report
- Version change: 0.1.0 -> 1.0.0
- Modified principles: 새 원칙 추가 - 스펙 우선, 테스트 필수, 설정 분리, 추적 가능한 커밋, 단순성, 한국어 문서 원칙
- Added sections: 추가 제약, 개발 워크플로우
- Removed sections: 없음
- Templates requiring updates: [.specify/templates/plan-template.md] ✅ updated, [.specify/templates/spec-template.md] ✅ updated, [.specify/templates/tasks-template.md] ✅ updated, [.specify/templates/checklist-template.md] ✅ updated
- Follow-up TODOs: 없음
-->

# Todo SDD Constitution

## Core Principles

### 1. 스펙 우선
모든 기능은 구현 전에 스펙 문서로 정의한다. 스펙에 명시되지 않은 기능은 구현하지 않는다.
- 판정 기준: 구현 시작 전 스펙 문서가 존재하고, 코드 변경 내역이 스펙 범위를 벗어나지 않는다. 스펙에 없는 기능이 추가되면 위반이다.

### 2. 테스트 필수
핵심 기능(추가/완료 토글, 삭제, 남은 개수, 필터)은 pytest 자동화 테스트로 검증한다.
- 판정 기준: 해당 핵심 기능에 대한 pytest 테스트가 존재하고 통과한다. 테스트가 없거나 실패하면 구현 완료로 인정하지 않는다.

### 3. 설정 분리
데이터베이스 경로 등 환경설정 값은 .env 파일로 관리하고 저장소에 커밋하지 않는다.
필요한 환경변수는 .env.example 파일에 문서화한다.
- 판정 기준: 설정값이 코드에 하드코딩되지 않고 .env/.env.example 기준으로 관리된다. 민감 정보가 저장소에 포함되면 위반이다.

### 4. 추적 가능한 커밋
모든 커밋 메시지는 태스크 ID로 시작한다. 형식은 "TXX: ..." 이다.
- 판정 기준: 커밋 메시지 앞에 태스크 ID가 포함된다. 태스크 ID 없이 커밋하면 위반이다.

### 5. 단순성
요구사항에 없는 기능이나 라이브러리는 임의로 추가하지 않는다.
- 판정 기준: 해결하려는 문제와 직접 관련 없는 기능이나 라이브러리 추가가 없고, 가장 단순한 구현 경로가 우선된다.

### 6. 한국어 문서 원칙
이 프로젝트에서 생성되는 모든 문서(constitution, spec, plan, tasks, checklist, 분석 리포트 등)는 반드시 한국어로 작성한다.
- 판정 기준: 생성된 문서의 제목, 설명, 기준, 체크리스트가 한국어로 작성된다. 외국어 혼용이나 영어 원문만 남기는 경우 위반이다.

## 추가 제약
- 문서와 코드 변경은 항상 관련된 스펙과 원칙을 기준으로 검토한다.
- 구현 변경이 기존 스펙을 벗어나면 반드시 스펙을 업데이트하고 그 이유를 기록한다.
- 테스트가 필요한 기능은 구현 전에 테스트를 먼저 작성한다.

## 개발 워크플로우
- 구현 전: 스펙 확인, 필요 시 스펙 업데이트, 테스트 계획 수립.
- 구현 중: 핵심 기능에 대한 테스트를 함께 작성하고, 환경설정은 .env/.env.example 기준으로 관리한다.
- 구현 후: 커밋 메시지에 태스크 ID를 포함하고, 문서와 코드를 한국어로 유지한다.

## Governance
이 Constitution은 프로젝트의 개발 기준을 우선한다. 모든 변경은 문서로 기록하고, 변경 전후의 영향 범위를 명확히 해야 한다.
- Amendment procedure: 원칙 변경은 먼저 문서(constitution/spec/plan/tasks)로 이유와 영향 범위를 기록한 뒤 승인한다.
- Versioning policy: 의미 있는 원칙 추가/수정은 MINOR, 문구 수정이나 비의미적 정정은 PATCH로 관리한다. 삭제 또는 근본적 재정의는 MAJOR로 관리한다.
- Compliance review: 구현 완료 전, 관련 테스트와 문서 기준을 확인하여 위반이 없는지 검토한다.

**Version**: 1.0.0 | **Ratified**: 2026-07-12 | **Last Amended**: 2026-07-12
