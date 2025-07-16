📅 2025.07.17

 # 🔐 AI 모델 생애주기에서 보안은 어떤 역할을 할까?

AI 시스템에 대한 공격을 효과적으로 방어하기 위해서는, **AI 모델의 전체 생애주기를 포괄하는 명확한 운영 절차**를 수립하는 것이 중요합니다.

강력하고 신뢰할 수 있으며 반복 가능한 AI 모델을 개발하고 배포하는 과정은 **여러 단계와 다양한 팀, 개발자, 이해관계자들의 협업**을 필요로 합니다.

---

## 📦 DevOps와 MLOps의 비교

소프트웨어 개발 및 운영에서 사용되는 **DevOps** 개념처럼, **MLOps (Machine Learning Operations)**는 **재현 가능하고 유연한 AI 모델을 배포**하기 위한 최적의 방법론과 도구들을 정의합니다.

---

## 🔁 CRISP-ML(Q): 품질 관리를 포함한 표준 AI 개발 프로세스

MLOps 중심의 대표적인 모델 개발 파이프라인으로는 **CRISP-ML(Q)**이 있습니다.  
이는 "Cross-Industry Standard Process for Machine Learning applications with Quality assurance"의 약자로, 품질 보증이 포함된 머신러닝 개발을 위한 산업별 통합 표준 절차입니다.

---

### 📘 CRISP-ML(Q)의 6단계 모델 생애주기

1. **비즈니스 및 데이터 이해 (Business and Data Understanding)**  
   - 문제 정의, 목표 설정, 데이터 원천 파악

2. **데이터 엔지니어링 (Data Engineering / Preparation)**  
   - 데이터 수집, 정제, 가공, 전처리

3. **머신러닝 모델 개발 (Machine Learning Model Engineering)**  
   - 알고리즘 선택, 모델 훈련, 성능 측정

4. **품질 보증 (Quality Assurance)**  
   - 모델에 대한 테스트, 검증, 리스크 평가

5. **배포 (Deployment)**  
   - 운영 환경에 모델 탑재 및 배치

6. **모니터링 및 유지보수 (Monitoring and Maintenance)**  
   - 모델의 실시간 성능 모니터링, 이상 탐지, 업데이트

> 📌 참고 이미지  
> **CRISP-ML(Q)** 머신러닝 생애주기 프로세스 (출처: visenger / CC BY 4.0)
<img width="2701" height="1499" alt="image" src="https://github.com/user-attachments/assets/64d469c6-199b-4c23-9bd1-4c8256b2c3c4" />

---

### 🔄 반복적 순환과 리스크 기반 접근

각 단계는 단순히 선형적으로 진행되는 것이 아니라, 다음과 같은 순환 구조를 가집니다:

- 먼저 **요구사항 및 제약 조건 정의**
- 이후 **리스크 식별 → 리스크 평가 → 리스크 완화**
- 요구사항을 충족할 때까지 반복
- 이해관계자의 요구나 환경 변화가 발생하면 이전 단계로 **되돌아가 반복적으로 수행**

---

### 🧩 모니터링 및 유지보수 단계의 중요성

실제 운영 환경에서는 다음과 같은 변화 요소들이 발생할 수 있습니다:

- **개념 드리프트 (Concept Drift):** 문제 정의 또는 데이터 패턴의 본질적인 변화  
- **데이터 드리프트 (Data Drift):** 입력 데이터 분포의 변화  
- **악의적 행동 또는 공격**

이러한 현실 세계의 변화에 대응하기 위해 **모델 생애주기를 역방향으로 돌아가 반복**하며 수정하는 것이 예상됩니다.

---

## 🛡 ATLAS는 CRISP-ML(Q)에 기반한 보안 가이드를 제공합니다

MITRE ATLAS는 각 보안 완화 전략(Mitigation)을 **CRISP-ML(Q)의 단계별로 연결(Tagging)**하여,  
각 팀이 자신이 담당하는 단계에서 예상되는 보안 취약점을 식별하고 **적절한 대처 방법**을 찾을 수 있도록 돕습니다.

> 📖 더 깊이 있는 이해를 원한다면 [CRISP-ML(Q) 원문 논문](https://arxiv.org/abs/2005.00397)도 참조해 보세요.

---

<sub>출처: [MITRE ATLAS - AI Security 101](https://atlas.mitre.org/resources/ai-security-101) 
