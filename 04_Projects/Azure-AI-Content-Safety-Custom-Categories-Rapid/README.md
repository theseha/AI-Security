📅 2025.11.23

# Azure AI Content Safety - Custom Categories (Rapid) 가이드

## 개요

Azure AI Content Safety의 Custom Categories 기능을 사용하면 사용자 정의 콘텐츠 분류 기준을 설정하여 특정 유형의 콘텐츠를 탐지할 수 있습니다. 이 문서에서는 한글 지원이 가능한 Rapid 버전의 Custom Categories 사용 방법을 다룹니다.

## Custom Categories 버전 비교

Azure AI Content Safety의 Custom Categories는 두 가지 버전으로 제공됩니다:

| 구분 | Standard | Rapid |
|------|----------|-------|
| **지원 언어** | English만 지원 | 다국어 지원 (한글 포함) |
| **처리 속도** | 상대적으로 느림 | 빠른 처리 속도 |
| **구현 방식** | SDK 지원 | REST API만 지원 |
| **적용 대상** | 영어 콘텐츠 필터링 | 다국어 콘텐츠 필터링 |

> **중요**: Standard 버전은 영어에 대해서만 지원하기 때문에, **한글로 된 Custom Category를 생성하기 위해서는 Rapid 버전을 사용해야 합니다**.

📚 참고: [Custom categories in Azure AI Content Safety (preview)](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/custom-categories)

## 지역(Region) 요구사항

Custom Categories (Standard 및 Rapid 모두)는 **한국(Korea) 리전을 지원하지 않습니다**. 따라서 해당 기능을 사용하기 위해서는 지원되는 다른 리전에 Azure AI Content Safety 인스턴스를 별도로 생성해야 합니다.

지원 리전에 대한 자세한 정보는 Microsoft Learn 문서를 참조하시기 바랍니다.

## 구현 방법

### SDK 지원 여부

Rapid 버전은 **별도 SDK가 지원되지 않으며**, **REST API 호출 방식**으로만 구현 가능합니다.

📚 참고: [Use the custom categories (rapid) API (preview)](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/how-to/custom-categories-rapid)

### 구현 단계

Custom Categories (Rapid)를 사용하기 위한 전체 프로세스는 다음과 같습니다:

#### 1. Incident 생성
- Custom Category는 **"Incident"**라는 단위로 관리됩니다
- 하나의 Category = 하나의 Incident
- 먼저 탐지하고자 하는 콘텐츠 유형에 대한 Incident를 생성합니다

#### 2. Sample 업로드
- 생성된 Incident에 학습용 샘플 데이터를 업로드합니다
- 샘플은 탐지하고자 하는 콘텐츠의 예시들입니다

#### 3. 배포 (Deployment)
- 샘플 업로드가 완료되면 Incident를 배포합니다
- 배포가 완료되어야 실제 탐지 API를 사용할 수 있습니다

#### 4. Incident Detection API 호출
- 배포된 Incident를 사용하여 콘텐츠를 분석합니다
- REST API를 통해 탐지 요청을 보냅니다

## API 응답 형식

Incident Detection API를 호출하면 다음과 같은 형식으로 결과가 반환됩니다:

```json
{
  "incidentMatches": [
    {
      "incidentName": "your-incident-name"
    }
  ]
}
```

### 응답 필드 설명
- `incidentMatches`: 탐지된 Incident 목록
- `incidentName`: 매칭된 Incident의 이름

## 향후 개선 사항

현재 Rapid 버전은 Preview 단계로, 응답에 Incident 매칭 여부만 포함됩니다. 향후 **Confidence Score(신뢰도 점수)**가 함께 제공된다면, 더 정교한 콘텐츠 필터링 제어가 가능할 것으로 예상됩니다.

예상되는 개선된 응답 형식:
```json
{
  "incidentMatches": [
    {
      "incidentName": "your-incident-name",
      "confidenceScore": 0.95
    }
  ]
}
```

## 활용 시나리오

Custom Categories (Rapid)는 다음과 같은 상황에서 유용합니다:

- 한글 콘텐츠에 대한 맞춤형 필터링이 필요한 경우
- 특정 도메인이나 조직에 특화된 콘텐츠 분류 기준이 있는 경우
- 기본 제공되는 Content Safety 카테고리로 충분하지 않은 경우
- 빠른 응답 속도가 요구되는 실시간 콘텐츠 모더레이션

## 참고 자료

- [Custom categories in Azure AI Content Safety (preview)](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/custom-categories)
- [Use the custom categories (rapid) API (preview)](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/how-to/custom-categories-rapid)

---

> **Note**: 이 문서는 Azure AI Content Safety의 Preview 기능을 다루고 있습니다. 기능 및 API 스펙은 정식 출시 시 변경될 수 있습니다.
