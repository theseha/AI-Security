📅 2025.07.26

# 🧪 Microsoft의 AI Red Teaming Playground Labs로 Prompt 공격 실험하기

LLM(대형 언어 모델)을 도입한 서비스가 점점 늘어나면서, 보안 취약점에 대한 실험과 대비가 필수적인 시대가 되었습니다. 이에 따라 Microsoft는 오픈소스로 [**AI Red Teaming Playground Labs**](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs/tree/main?tab=readme-ov-file)를 공개하여, 누구나 LLM 대상의 **Prompt 공격**을 직접 실험해볼 수 있는 환경을 제공합니다.

<img width="796" height="344" alt="AI Red Teaming Playground Labs" src="https://github.com/user-attachments/assets/5e6af8ad-56c4-4549-99f2-6874edb90b05" />

---

## 🎮 Lakera의 Gandalf 이후, 한 단계 더 진화된 실험

처음 **LLM Security**가 화두가 되었을 당시, 일반 사용자들이 쉽게 접근하고 실험할 수 있도록 만든 것이 바로 **Lakera의 Gandalf Game**입니다.  
게임처럼 재미있게 접근할 수 있고, 한글로도 실험이 가능해 많은 사람들의 관심을 끌었습니다.

하지만 이후 다양한 Prompt 공격이 등장하면서, 단순한 실험 이상의 시뮬레이션이 필요해졌습니다.

---

## 🚨 진화하는 Prompt 공격: 다양한 시나리오를 실험할 수 있는 Playground

Microsoft의 AI Red Teaming Playground Labs에서는 다음과 같은 공격 기법들을 시나리오별로 실험할 수 있습니다:

- **Crescendo Attack**
- **Indirect Prompt Injection**
- **Encoding / 암호화 기법 활용**
- 그 외 최신 전략들

총 **12개의 시나리오**가 준비되어 있으며, 각 시나리오는 특정 공격 기법을 사용해 시스템의 비밀번호를 알아내는 미션으로 구성되어 있습니다.

---

## 🧑‍💻 실험 방법

1. GitHub에서 Labs를 Cloning 합니다:  
   👉 [Microsoft AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs/tree/main?tab=readme-ov-file)

2. 가이드에 따라 설치 및 실행합니다.

3. 각 시나리오를 실행하면, 채팅창으로 이동하며 미션이 주어집니다.

4. **gpt-4o 모델**을 기본으로 설정하여 실험을 진행하면 됩니다.

5. 💬 한글로도 실험이 가능하므로, 실제 환경과 유사하게 테스트할 수 있습니다.

---

<img width="959" height="454" alt="Lab 1" src="https://github.com/user-attachments/assets/1129027e-71f9-43bd-bcb7-4d0ffa1eb17a" />

## 📌 정리

AI 보안을 고려하는 조직이나 개인에게 이 Labs는 훌륭한 학습 도구입니다.  
단순한 게임이 아닌, **고도화된 공격 기법**을 직접 다뤄보며 보안의 본질을 체험할 수 있습니다.  
보안이 단순히 방어적 조치에 그치지 않고, 실험과 탐구를 통해 **공격자처럼 생각하는 시도**가 필요하다는 것을 알려주는 훌륭한 예시입니다.
