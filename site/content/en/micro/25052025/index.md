---
title: "AI memory for learning"
date: 2025-05-25T19:55:00+02:00
platform: "X"
external_url: "https://x.com/davidlmsEN/status/1926698704855011674"
tags: ["x", "micro"]
---

Imagine studying with AI for months, but every conversation starts from scratch. The model helps you well… but doesn't remember you've mastered algebra while struggling with trigonometry. We have "memory" in LLMs, but not for learning.

When you search for AI in education, you find the same everywhere: pre-made prompts, task automation, automatic grading... 
@emollick has written extensively about this challenge of moving beyond surface-level AI integration in classrooms.

There are promising initiatives like 
@karpathy´s @EurekaLabsAI that I'm excited about. But there's one specific aspect I find fascinating: applying LLM memory concepts specifically to learning progression tracking.

The challenge isn't just technical—it's about creating persistent learning context. What if AI could maintain a structured understanding of your learning journey, not just remember previous chats, but actual competency development?

Following research on AI teaching approaches, I realized we need systems that bridge AI interactions with educational standards. This led me to explore xAPI—the learning analytics specification.

xAPI enables something powerful: learning records that flow between systems. Your AI tutor sessions, LMS activities, even browser-tracked learning resources can contribute to a unified learning portrait.

So I built LearnMCP-xAPI: a bridge between AI agents and learning record stores. It's one piece of the puzzle we need to build—connecting AI memory concepts with established learning analytics infrastructure.

The AI can record structured learning evidence: "practiced quadratic equations level 2," "achieved Python recursion mastery," "needs trigonometry reinforcement"—all flowing into systems teachers already use.

I've tested it with LRS SQL, but it works with any xAPI-compliant LRS and any MCP client. The goal: making AI learning-aware through standards, not proprietary solutions.

[Released on GitHub](https://github.com/DavidLMS/learnmcp-xapi).

What if AI could truly be your long-term learning companion, not just your tutor of the moment? That's the question I'm trying to answer.