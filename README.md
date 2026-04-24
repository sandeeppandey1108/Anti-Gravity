# Anti-Gravity: Autonomous AI Cinematic Media System

Anti-Gravity is a fully autonomous AI-driven cinematic media company pipeline. It is designed to research trends, generate scripts, produce cinematic videos, create thumbnails, and optimize for performance using a multi-AI orchestration approach.

## 🚀 Project Vision
The goal is to build a self-managing system that:
1. **Researches** viral trends and competitor patterns.
2. **Generates** high-quality cinematic scripts and hooks.
3. **Produces** videos with synced audio and visuals.
4. **Optimizes** thumbnails and titles for maximum CTR.
5. **Learns** from performance data to improve over time.

## 📂 Repository Structure
- `agents/`: AI agents for research and script generation.
- `core/`: The engine of the system (orchestrator, video pipeline, TTS, thumbnails).
- `docs/`: Comprehensive guides, workflows, and API setup instructions.
- `n8n/`: Automation workflows for scheduled tasks.
- `prompts/`: Master prompts for the AI agents.
- `python/`: Runner scripts and entry points.
- `system/`: Memory, scoring, and engine configurations.
- `vision_and_notes.txt`: Original project vision and development notes.

## 🛠️ Getting Started
1. **Setup Environment**: Install dependencies from `requirements.txt`.
2. **Configure APIs**: Follow `docs/youtube_api_setup.md` and `docs/n8n_import_guide.md`.
3. **Run the System**:
   ```bash
   python core/orchestrator.py
   ```

## 🧠 Core Architecture
The system uses an **Orchestrator Agent** to manage specialized agents:
- **Research Agent**: Finds trends and analyzes competitors.
- **Production Agent**: Handles script, voice, video, and thumbnails.
- **Analytics Agent**: Tracks performance and updates the **Memory System**.
- **Quality Agent**: Ensures content meets high standards before publishing.

## ⚠️ Safety & Guardrails
This system is designed with control layers to prevent account flagging and ensure content quality. Always review the `vision_and_notes.txt` for the grounded development philosophy.

---
*Built for the future of autonomous content creation.*
