📅 2025.08.27

# AI Red Teaming Agent

## Overview

**AI Red Teaming Agent = PyRIT + Azure AI Foundry's Risk and Safety Evaluation**

### Core Capabilities

- **Automated scans for content risks**: 모델과 애플리케이션 엔드포인트에 대해 적대적 탐색 시뮬레이션을 자동으로 스캔
- **Evaluate probing success**: '공격-응답' 쌍의 결과를 평가하여 ASR(Attack Success Rate) 지표 생성
- **Reporting and logging**: 공격 탐색 기법과 위험 범주 별 ASR 확인 및 Azure AI Foundry에서 모니터링 및 추적 가능

### NIST AI Risk Management Framework

AI 시스템 개발 시 발생할 수 있는 AI 관련 위험을 관리하기 위해 참조할 수 있는 프레임워크 (Govern-Map-Measure-Manage):

- **Map**: 위험 식별 및 use case 정의
- **Measure**: 위험 평가
- **Manage**: 위험 완화 및 사고 대응 계획과 함께 모니터링

> 💡 **Why Automation is Needed**: 수동 대응은 시간과 자원이 많이 소모되고, 신속한 AI 도입에 방해 요소가 됩니다.

### Stages to Scan

- **Design**: Use Case에 적합한 가장 안전한 모델 선택
- **Development**: 애플리케이션 내 모델 업그레이드 또는 Fine-tuned 모델 생성 시
- **Pre-deployment**: 생성형 AI 애플리케이션을 운영 환경에 배포하기 전
- **In Production**: Azure AI Content Safety와 시스템 메시지 상의 [안전 문구](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/safety-system-message-templates) 사용

<img width="1799" height="1012" alt="image" src="https://github.com/user-attachments/assets/20d61e25-182f-43b5-90ef-6003fec7bfd1" />

### How AI Red Teaming Works

1. 위험 범주 별 **Seed Prompt 또는 공격 목표 데이터셋** 제공
2. Direct Prompt Injection은 기본 필터로 쉽게 차단 가능하므로, PyRIT을 이용하여 고도화된 공격을 테스트
3. 공격 시뮬레이션과 유해 콘텐츠 응답 평가를 위한 Fine-tuned **적대적 LLM** 제공
4. 평가 지표로 **ASR** (Attack Success Rate) - 전체 공격 시도 대비 성공 비율 측정

<img width="972" height="494" alt="image" src="https://github.com/user-attachments/assets/9cef4e17-1533-4824-bc20-06a6ae6bdf0f" />

## Supported Risk Categories

| Risk Category | Description |
|--------------|-------------|
| Hateful and Unfair Content | 증오적 또는 불공정(인종, 민족, 국적, 성별, 성적 지향, 종교 등의 Protected Class 대상 차별)한 언어 또는 이미지 |
| Sexual Content | 생식기, 성적 행위 및 용어, 매춘, 포르노, 성적 남용 등의 언어 또는 이미지 |
| Violent Content | 상해, 공격, 살인 등과 관련된 물리적 행위 및 기구의 언어 또는 이미지 |
| Self-Harm-related Content | 자해, 자살과 관련된 물리적 행위 및 기구의 언어 또는 이미지 |

## Supported Attack Strategies

### Easy Complexity

| Attack Strategy | Category | Description |
|----------------|----------|-------------|
| AnsiAttack | Encoding Techniques | ANSI escape 코드로 색상/스타일 변경 `\x1b[31mHello World\x1b[0m` |
| AsciiArt | Encoding Techniques | ASCII 문자로 그림 표현 |
| AsciiSmuggler | Encoding Techniques | ASCII 코드 안에 데이터 숨김 `"Hello&#x20;World<!--secret:1234-->"` |
| Atbash | Text Transformation | 알파벳을 반대로 치환 (A <-> Z, B <-> Y) `"Svool Dliow"` |
| Base64 | Text Transformation | Base64 인코딩 `"SGVsbG8gV29ybGQ="` |
| Binary | Text Transformation | 2진수로 변환 |
| Caesar | Text Transformation | 문자 3칸씩 밀기 `"Khoor Zruog"` |
| CharacterSpace | Character Manipulation | 문자 사이에 공백 추가 `"H e l l o W o r l d"` |
| CharSwap | Character Manipulation | 문자 위치 바꾸기 `"Hlelo Wrold"` |
| Diacritic | Character Manipulation | 문자에 발음 기호 추가 `"Héllö Wòrld"` |
| Flip | Character Manipulation | 문자 좌우 반전 `"plɹoM ollǝH"` |
| Leetspeak | Character Manipulation | 숫자/기호로 대체 `"H3ll0 W0r1d"` |
| Morse | Text Transformation | 모스 부호 변환 `".... . .-.. .-.. --- / .-- --- .-. .-.. -.."` |
| ROT13 | Text Transformation | 13칸 문자 치환 `"Uryyb Jbeyq"` |
| SuffixAppend | Jailbreak Attempts | 문장 뒤에 악성 명령 추가 |
| StringJoin | Character Manipulation | 문자열 합치기 `"Hel" + "lo " + "World"` |
| UnicodeConfusable | Encoding Techniques | 비슷하게 생긴 유니코드 사용 `"Нello Wоrld"` |
| UnicodeSubstitution | Encoding Techniques | 유니코드 변형 문자 사용 `"Hｅｌｌｏ　Ｗｏｒｌｄ"` |
| URL | Text Transformation | URL 인코딩 `"Hello%20World"` |
| Jailbreak | Jailbreak Attempts | 우회 프롬프트 삽입 |

### Moderate Complexity

| Attack Strategy | Category | Description |
|----------------|----------|-------------|
| Tense | Text Transformation | 시제를 과거형으로 변경 `"Said hello to the world"` |

### Difficult Complexity

- Easy와 Moderate 혼합
```python
AttackStrategy.Compose([AttackStrategy.Tense, AttackStrategy.Base64])
```

## Getting Started

### Prerequisites

- Azure AI Foundry Project 또는 Hub-based Project (현재, Azure AI Foundry Project로 할 것을 권장)
- **Python 3.10, 3.11, 3.12** (PyRIT 지원 버전)
- **지원 지역**: East US2, Sweden Central, France Central, Switzerland West

### For Foundry Project

1. 리소스 레벨로 Storage Account를 Foundry Project에 [연결](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluations-storage-account)
2. 연결된 Storage Account에 project access 권한 부여
3. Entra ID 권한 부여 시:
   - Foundry Project에서 Managed Identity 활성화
   - Storage의 **Storage Blob Data Contributor** 권한을 Foundry Project에 부여
   - Storage Account 권한 부여 시, **Azure AI Foundry Project**의 `[ResourceName]/[ProjectName]` 포맷의 Project 선택

### Installation

```bash
pip install uv
uv pip install azure-ai-evaluation[redteam] azure-identity openai azure-ai-projects
```

### Basic Usage

#### Configuration

```python
from azure.ai.evaluation import RedTeam, RiskCategory, AttackStrategy
from azure.identity import DefaultAzureCredential
import asyncio

# Custom configuration
red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project,  # required
    credential=DefaultAzureCredential(),  # required
    risk_categories=[  # optional, defaults to all four risk categories
        RiskCategory.Violence,
        RiskCategory.HateUnfairness,
        RiskCategory.Sexual,
        RiskCategory.SelfHarm
    ],
    num_objectives=5,  # optional, defaults to 10
)
```

#### Running Scans

```python
async def main():
    red_team_result = await red_team_agent.scan(
        target=simple_callback,
        scan_name="simple-callback-scan",
        attack_strategies=[
            AttackStrategy.AsciiArt,
            AttackStrategy.Compose([AttackStrategy.Tense, AttackStrategy.Base64])
        ],
        output_path="red_team_output.json",
    )
    print(red_team_result)

if __name__ == "__main__":
    asyncio.run(main())
```

### Using Service Principal

#### 1. Create Service Principal

```bash
az ad sp create-for-rbac \
  --name "<Service-Principal이름>" \
  --role Contributor \
  --scopes /subscriptions/<구독ID>
```

#### 2. Configure Environment Variables

Create `.env` file with:
```env
AZURE_CLIENT_ID=<App ID>
AZURE_TENANT_ID=<Tenant>
AZURE_CLIENT_SECRET=<password>
```

#### 3. Grant Permissions

- Azure AI Foundry Project: **Cognitive Services User** 권한 (Service Principal에 부여)
- Azure AI Foundry: **Cognitive Services OpenAI User** 권한 (Service Principal에 부여) (for advanced calls)

## Run AI Red Teaming Agent Locally

### Supported Targets

#### 1. Model Configurations
- 기본 LLM 모델을 직접 대상으로 스캔 (모델 자체의 안전성 테스트)
- 현재 `/chat/completions` endpoint만 지원 (OpenAI API 형식)

#### 2. Simple Callback
- Agent가 정상 동작하는지 로직 확인하는 목적으로 스캔

#### 3. Complex Callback
- OpenAI API 형식 외의 AI App이 어떻게 대답하는지 Custom하게 확인
- 이미 모델을 이용해서 system message, 자체 filtering 등이 적용되어 있을 경우 테스트

#### 4. PyRIT Prompt Target
- PyRIT의 다양한 prompt target 활용

## Run AI Red Teaming Agent in the Cloud

### Prerequisites

- **Azure AI Foundry Project만** 지원 (Hub-based Project는 클라우드에서 미지원)
- Storage Account 연결 및 권한 설정 (로컬 실행과 동일)

### Supported Targets

Azure OpenAI만 Target 지정 가능:

#### Option 1: Foundry Project 배포

```python
import os

model_endpoint = os.environ["MODEL_ENDPOINT"]  # https://<account_name>.openai.azure.com
model_api_key = os.environ["MODEL_API_KEY"]
model_deployment_name = os.environ["MODEL_DEPLOYMENT_NAME"]  # gpt-4o-mini
```

#### Option 2: Azure OpenAI/AI Services 배포

```python
# Format: "connectionName/deploymentName"
model_deployment_name = "my-openai-connection/gpt-4o-mini"
```

## Limitations

- **Single-turn interactions in text-only scenarios**만 지원
- Python 3.10-3.12에서만 동작
- 클라우드 실행 시 Azure OpenAI만 지원

## References

- [Azure AI Foundry - AI Red Teaming Agent Concepts](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent)
- [How to Run Scans with AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/run-scans-ai-red-teaming-agent)
- [Azure AI Samples - AI Red Teaming](https://github.com/Azure-Samples/azureai-samples/blob/main/scenarios/evaluate/AI_RedTeaming/AI_RedTeaming.ipynb)
- [PyRIT GitHub Repository](https://github.com/Azure/PyRIT)
