📅 2025.07.17

# 🔒 AI 보안 주요 주제 (AI Security Topics)

AI 보안은 기술의 발전과 함께 계속해서 진화하는 분야입니다. 특히 최근에는 아래 세 가지 하위 분야에서 빠르게 발전이 이루어지고 있습니다.

---

## 🧠 1. LLM 보안 (LLM Security)

**대규모 언어 모델(LLM, Large Language Models)**은 수천억 개의 단어를 학습해 자연어로 된 질문에 대해 텍스트, 이미지, 영상 등을 생성할 수 있는 모델입니다.  
2022년 11월 OpenAI의 **ChatGPT** 출시 이후, 콘텐츠 생성, 스타일 변환, 요약 등 다양한 복합 작업을 **단일 모델로 수행 가능한 능력** 덕분에 널리 알려지게 되었습니다.

### 🔐 보안 관점의 문제점

- **거대한 학습 데이터셋**, **불투명한 내부 구조**, **자연어를 활용한 프롬프트 입력** 등으로 인해 기존 AI보다 **복합적인 보안 문제**를 일으킵니다.
- 예를 들어, **간접적인 프롬프트 인젝션(Indirect Prompt Injection)**을 통해 **사용자의 개인정보(PII)를 추출**하거나, 악성 웹사이트로 유도하는 등의 방식이 대표적입니다.

### ⚠️ 관련 공격 유형 예시

- LLM Prompt Injection  
- LLM Plugin 탈취 (Compromise LLM Plugins)  
- LLM Jailbreak (모델 제약 해제)  

> 🆕 MITRE는 2023년 가을 ATLAS 업데이트를 통해 **LLM 공격 사례 중심의 섹션을 추가**하였으며, 외부 논문/도구/사례 리스트도 별도로 제공하고 있습니다.

---

## 🔧 2. 하드웨어 보안 (Hardware Security)

하드웨어 보안은 기존 사이버보안 분야에서 잘 연구되어 온 분야이며, **AI 시스템 보안과의 접점**에서도 주목받고 있습니다.

### 💣 대표적인 하드웨어 공격 유형

- **사이드 채널 공격 (Side Channel Attacks)**  
  전류/전압/처리 속도 등의 **간접 정보(부채널)를 통해 시스템 내부 정보를 추측**

- **결함 주입 공격 (Fault Injection Attacks)**  
  물리적 환경 조작이나 비정상적 입력을 통해 모델 동작을 **고의로 왜곡**

- **하드웨어 트로이 목마 (Hardware Trojan Attacks)**  
  GPU나 기타 칩셋 등에 **악성 백도어 회로 삽입**

### 📚 추천 참고자료

- Zhou et al. (2021) — *Deep Neural Network Security From a Hardware Perspective*  
- Xu et al. (2021) — *Security of Neural Networks from Hardware Perspective: A Survey and Beyond*

---

## 🚗 3. 자율 시스템 보안 (Autonomous Systems)

MITRE ATLAS 팀은 현재 **AI 보안과 자율 시스템의 교차점**에 대한 연구를 진행 중입니다.

### 🚘 자율 시스템 보안 전략

- 자율 시스템은 **센서, 결합 알고리즘, 판단 시스템** 등 **여러 구성 요소로 이루어진 스택(Autonomy Stack)** 형태로 구성됩니다.
- 각 구성 요소에 대한 위험 요소를 파악하면 **AI가 통합된 지점과 보안 취약점**을 보다 명확히 인식할 수 있습니다.

> ▶️ [AI Security for Autonomous Systems 페이지](https://atlas.mitre.org/resources/ai-security-101)를 참고하면 자율 시스템 구성요소별 상세 설명을 확인할 수 있습니다.

---

## ⚠️ 4. AI의 악의적 활용: 사이버 도메인 (Malicious Use of AI - Cyber Domain)

최근에는 **사이버 공격 체인 개발에 AI(특히 생성형 모델)가 사용되는 사례**가 증가하고 있습니다.

MITRE ATLAS는 이에 대해 **"AI의 악의적 사이버 활용(Malicious Use of AI for Cybersecurity)"**이라는 이름으로 별도 영역으로 식별하고 있으며, 기존의 ATLAS/ATT&CK에서는 아직 완전히 구조화되지 않은 상태입니다.

### 🔍 연구 방향 및 사례

- 공격자가 ChatGPT 등 생성형 AI를 활용하여 **공격 코드 작성, 피싱 콘텐츠 자동 생성, 취약점 조사 자동화** 등을 수행
- 특히 **공급망(Supply Chain)** 또는 **핵심 인프라(Critical Infrastructure)**에 대한 비대칭적 공격 가능성 존재

> MITRE는 해당 위협 사례들을 분석하여, 향후 **ATLAS/ATT&CK 프레임워크와의 연결 지점 탐색 및 신규 매트릭스 개발**을 추진 중입니다.

---

<sub>출처: [MITRE ATLAS - AI Security Topics](https://atlas.mitre.org/resources/ai-security-101) 
