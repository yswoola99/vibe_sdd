# API 계약서: 오늘의 할 일 웹 앱

## 공통 규칙

- 모든 응답은 JSON 형태로 반환한다.
- 에러 응답은 `detail` 또는 `message` 필드로 사용자에게 전달 가능한 메시지를 포함한다.
- `GET /health`는 상태 확인용이며 `{"status": "ok"}` 형태로 응답한다.

## 엔드포인트

### GET /api/todos

목록 조회.

**쿼리 파라미터**
- `status`: `all` | `active` | `completed`

**성공 응답**
```json
[
  {
    "id": 1,
    "title": "회의 준비",
    "completed": false,
    "created_at": "2026-07-12T10:00:00",
    "updated_at": "2026-07-12T10:00:00"
  }
]
```

### POST /api/todos

새 할 일 생성.

**요청 본문**
```json
{ "title": "회의 준비" }
```

**성공 응답**
```json
{
  "id": 1,
  "title": "회의 준비",
  "completed": false,
  "created_at": "2026-07-12T10:00:00",
  "updated_at": "2026-07-12T10:00:00"
}
```

**오류 응답**
- 제목이 비어 있거나 공백인 경우: `422 Unprocessable Entity`

### PATCH /api/todos/{id}

완료 상태 토글.

**요청 본문**
```json
{ "completed": true }
```

**성공 응답**
```json
{
  "id": 1,
  "title": "회의 준비",
  "completed": true,
  "created_at": "2026-07-12T10:00:00",
  "updated_at": "2026-07-12T10:00:00"
}
```

**오류 응답**
- 존재하지 않는 ID: `404 Not Found`

### DELETE /api/todos/{id}

할 일 삭제.

**성공 응답**
```json
{ "message": "삭제되었습니다." }
```

**오류 응답**
- 존재하지 않는 ID: `404 Not Found`

### GET /

메인 화면 HTML 반환.

### GET /health

상태 확인 응답.
```json
{ "status": "ok" }
```
