📅 2025.07.29

# Microsoft Defender for Cloud: AI 위협 보호

Microsoft Defender for Cloud는 이제 생성형 AI 서비스에 대한 실시간 위협 감지와 보안을 강화하는 **AI Threat Protection** 기능을 제공합니다. 이 기능은 데이터 유출, 데이터 중독, 프롬프트 탈출(jailbreak), 자격 증명 도용과 같은 위협을 빠르게 식별하고 대응할 수 있도록 돕습니다.

## 🔐 AI 서비스에 대한 위협 탐지 및 대응

AI Threat Protection은 Microsoft의 **Threat Intelligence**와 **Azure AI Content Safety의 Prompt Shields**를 활용해 아래와 같은 위협을 탐지합니다:

- 민감한 데이터 유출
- 악의적 프롬프트 조작(Jailbreak)
- AI 모델 오남용
- 자격 증명 탈취
- 데이터 중독 공격

위협이 탐지되면 Defender for Cloud는 관련 보안 경고(Security Alerts)를 생성하고 개발자와 보안팀이 빠르게 대응할 수 있도록 가이드를 제공합니다.

## 🧠 Defender XDR와의 통합

이제 AI 서비스 위협 경고는 **Microsoft Defender XDR**과 통합되어, 보안팀은 단일 포털에서 모든 AI 워크로드의 경고를 확인할 수 있습니다. 이를 통해:

- AI 관련 사고와 일반 보안 사고를 연계 분석 가능
- 공격의 전체 흐름과 원인을 보다 정확하게 파악

<img width="1655" height="1129" alt="MDC3" src="https://github.com/user-attachments/assets/1116b406-4100-4ce0-a156-fc73bd0a8010" />

## ⚙️ 위협 보호 기능 활성화 방법

AI 서비스에 대한 위협 보호를 활성화하려면 아래 절차를 따르세요:

1. [Azure 포털](https://portal.azure.com) 접속
2. **Microsoft Defender for Cloud** 검색 및 선택
3. 왼쪽 메뉴에서 **Environment settings** 클릭
4. 관련된 Azure 구독 선택
5. **Defender plans** 페이지에서 **AI services** 토글을 **On**

<img width="851" height="596" alt="MDC1" src="https://github.com/user-attachments/assets/d77ff91f-98f7-42b7-8944-c203b46d097c" />

## 👁️ 사용자 프롬프트 증거 활성화

AI 서비스에 대한 경고에는 실제 사용자 입력 프롬프트와 모델 응답(증거)를 포함할 수 있습니다. 이를 통해 보안팀은:

- 의심스러운 사용자 의도를 분류하고
- 경고를 보다 정확히 판단할 수 있습니다.

사용자 프롬프트 증거는 Azure Portal, Defender 포털, 그리고 연결된 파트너 솔루션을 통해 확인할 수 있습니다.

## 📊 Microsoft Purview와의 연동을 통한 데이터 보안 강화

Microsoft Purview 라이선스를 통해 Azure AI 상의 프롬프트 및 응답 데이터를 분석 및 보호할 수 있습니다. 주요 기능은 다음과 같습니다:

- 민감 정보 유형(SIT) 자동 분류
- 사용자 활동 감시 및 규정 준수
- eDiscovery 및 감사 로그 확보
- 데이터 수명 주기 관리

> ⚠️ 주의: 해당 기능은 Microsoft Purview 라이선스가 필요하며, Microsoft Entra ID를 사용하는 API 호출에만 적용됩니다. [자세히 보기](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai)

<img width="858" height="263" alt="MDC4" src="https://github.com/user-attachments/assets/909a71c7-2f62-4dc9-9e5d-aed6264a0512" />

## 🧪 Azure AI Foundry와의 통합 (Preview)

Microsoft Defender for Cloud의 런타임 위협 탐지 경고가 **Azure AI Foundry 포털과 네이티브하게 통합**되었습니다. 이제 개발자는 워크플로우를 벗어나지 않고도 실시간 보안 경고와 추천 사항을 확인할 수 있습니다.

이 통합을 통해:

- 프로젝트 단위의 보안 가시성 확보
- 설정 오류 및 위협에 대한 즉각 대응
- 보안팀 대기 없이 개발자가 직접 위험 인식 및 조치

<img width="1432" height="801" alt="MDC2" src="https://github.com/user-attachments/assets/e4fe5ad4-6312-426d-a1a1-7f6188ba3e95" />

## 🔍 탐지 가능한 대표 위협 유형 (15종 이상)

- ASCII Smuggling 프롬프트 인젝션 탐지
- 프롬프트 탈옥 (Jailbreak) 탐지
- AI 리소스에 비정상 접근 탐지
- 인증정보 탈취 시도 탐지
- Tor IP에서의 비정상 접근 탐지 등

---

## 🔗 참고 문서

- [AI 위협 보호 개요 문서](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)
- [Microsoft Tech Community: Defender for Cloud AI 보안](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/secure-your-ai-applications-from-code-to-runtime-with-microsoft-defender-for-clo/4127665)
- [Azure AI Foundry와의 보안 통합 발표](https://techcommunity.microsoft.com/blog/microsoft-security-blog/enterprise-grade-controls-for-ai-apps-and-agents-built-with-azure-ai-foundry-and/4414757)
- [AI 사용자의 Context 수집 가이드](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai)
- [AI 워크로드 경고 항목들](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads)
