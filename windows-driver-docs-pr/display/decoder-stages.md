---
title: Decoder Stages
description: Decoder Stages
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , video decoding
- Video Acceleration WDK DirectX , video decoding
- VA WDK DirectX , video decoding
- decoding video WDK DirectX VA , decoder stages
- video decoding WDK DirectX VA , decoder stages
- decoder stages WDK DirectX VA
- inverse discrete-cosine transform WDK DirectX VA
- IDCT WDK DirectX VA
- MCP WDK DirectX VA
- motion compensation WDK DirectX VA
ms.date: 04/20/2017
---

# Decoder Stages

The decoder stages that are depicted in the following figure show the operation of the motion compensation prediction (MCP) and inverse discrete-cosine transform (IDCT) parts of an accelerator. The data indicated as dct_type is a syntax element that controls the type of IDCT that is performed.

:::image type="content" source="images/decstages.png" alt-text="Diagram showing the operation of motion compensation prediction and inverse discrete-cosine transform in a decoder.":::
