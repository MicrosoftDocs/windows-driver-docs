---
title: Audio measures
description: Audio measures filter out benign initialization errors during audio driver flighting
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Audio measures

## Description

The Windows Core Audio APIs introduce the concept of a **stream** as a connection between an application and an audio device that plays or captures audio, where a single application can have multiple audio streams. Every stream the application initializes is assigned to a **session**, which manages the input and output of each assigned stream. An application can call the Windows Core Audio API, which returns a success or failure code to indicate if the initialization was successful. These failure codes can be negligible, like the endpoint no longer existing, or severe where the initialization failed after encountering a bug.

Audio measures filter out benign initialization errors; a list of these errors is provided in the [appendix](/measure-appendix.md).
