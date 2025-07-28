📅 2025.07.28

# Azure AI Foundry에서 Deploy 가능한 Language Model 제한하기 — Azure Policy로 보안 강화

Azure AI Foundry에서는 오픈소스 및 상용 Language Model들을 빠르게 배포하고 사용할 수 있지만, 이들 모델이 항상 신뢰할 수 있는 것은 아닙니다. 최근에는 모델 자체에 **취약점이나 백도어(backdoor)**가 포함된 사례도 발견되고 있어, 사전 대응이 점점 더 중요해지고 있습니다.

---

## 🔍 Model Scanner만으로는 부족하다

Microsoft가 제공하는 **Model Scanner** 기능을 통해 일부 취약한 모델을 자동으로 탐지할 수 있지만, 모든 모델을 **스캔하지 못하거나**, **안전하다고 완전히 보장되지 않는** 경우도 존재합니다.

따라서, **스캐너로 검증되지 않은 모델**이 개발자에 의해 실수 또는 의도적으로 사용되지 않도록 **추가적인 제어 수단**이 필요합니다.

---

## ✅ Azure Policy로 Model 사용 제어하기

Azure는 **Policy** 기능을 통해 AI Foundry 환경에서 사용 가능한 Language Model을 직접 **제한**하거나, 사용을 **모니터링**할 수 있습니다.

---

## 🛠️ 적용 방법

### 1. Azure Portal에서 Policy 메뉴 진입

- Azure Portal 검색창에 `Policy`를 입력하고 이동합니다.

<img width="854" height="622" alt="Policy1" src="https://github.com/user-attachments/assets/f0b25f19-27f9-4cd4-bf96-6da339e9dfc2" />

### 2. 정책 정의 (Definition) 생성

- 좌측 메뉴에서 `Definitions`를 클릭
- **새로운 Definition을 생성**
- 아래와 같이 허용된 모델만 사용할 수 있도록 정책을 구성합니다.

<img width="848" height="631" alt="Policy2" src="https://github.com/user-attachments/assets/f57d20dc-6898-425c-9f94-9a1832bf0127" />

```json
{
  "mode": "All",
  "policyRule": {
    "if": {
      "allOf": [
        {
          "field": "type",
          "equals": "Microsoft.CognitiveServices/accounts/deployments"
        },
        {
          "not": {
            "field": "Microsoft.CognitiveServices/accounts/deployments/model.name",
            "in": "[parameters('allowedModels')]"
          }
        }
      ]
    },
    "then": {
      "effect": "audit"
    }
  },
  "parameters": {
    "allowedModels": {
      "type": "Array",
      "metadata": {
        "displayName": "Allowed models",
        "description": "The list of allowed models to be deployed."
      },
      "defaultValue": [
        "gpt-4.1",
        "gpt-4o",
        "text-embedding-ada-002"
      ]
    }
  }
}
```
✅ allowedModels 항목에 허용하고자 하는 정확한 모델 ID(예: "openai/gpt-4")를 입력하세요.

### 3. 정책 할당 (Assignment)

- 생성한 Definition을 원하는 범위에 할당할 수 있습니다:
  - **Subscription**
  - **Resource Group**

<img width="853" height="629" alt="Policy3" src="https://github.com/user-attachments/assets/6d6c77c2-44ca-4772-9734-9c573559be81" />

- 할당 시 `allowedModels` 값도 함께 설정해야 합니다.

### ⚙️ 적용 결과

- **정책은 수 초 내로 적용**됩니다.
- `allowedModels` 목록에 포함되지 않은 모델을 배포하려고 하면, 해당 요청은 **자동으로 실패(Deny)** 됩니다.

<img width="854" height="653" alt="Policy5" src="https://github.com/user-attachments/assets/23ec403f-9b45-44ff-849a-ef7db32846ee" />

---

### 👁️ 감시(Audit)도 가능

- 정책의 `effect`를 `"audit"`으로 설정하면, **실제 배포는 허용되지만 정책 위반 여부는 로깅**됩니다.
- 이 설정은 정책을 적용하기 전에 조직 내 어떤 모델이 사용되고 있는지 **파악하고 분석**할 때 유용합니다.
- Azure Policy의 **Compliance 대시보드**에서 정책 위반 리소스를 시각적으로 확인할 수 있어, 지속적인 모니터링이 가능합니다.

<img width="848" height="629" alt="Policy4" src="https://github.com/user-attachments/assets/36b5a48d-870c-4642-b08d-34babb956b5c" />

---

### 📌 참고 문서

- [📄 Azure Machine Learning: 사용자 정의 정책으로 모델 배포 제어하기](https://docs.azure.cn/en-us/machine-learning/how-to-custom-policy-model-deployment?view=azureml-api-2)
- [📘 Azure Policy 공식 문서](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

### ✅ 마무리

Azure AI Foundry에서 제공하는 다양한 Language Model은 생산성과 효율성을 높일 수 있지만,  
**보안이 검증되지 않은 모델 사용은 심각한 리스크**로 이어질 수 있습니다.

Microsoft의 **Model Scanner**를 통한 위협 탐지와 함께,  
**Azure Policy를 이용해 신뢰할 수 있는 모델만 사용하도록 강제하거나 감시**함으로써  
보다 안전한 생성형 AI 환경을 구축할 수 있습니다.

> 🔐 지금 바로 Azure Policy를 설정하여 **책임 있고 안전한 AI 개발 환경**을 실현해 보세요!
