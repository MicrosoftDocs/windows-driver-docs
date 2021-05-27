---
title: Fingerprint measures
description: Fingerprint measures look at the success of the user experience using fingerprint devices
ms.topic: article
ms.date: 03/30/2020 
ms.localizationpriority: medium
---

# Fingerprint measures

## Description

The [Windows Biometric Framework (WBF)](/windows/win32/secbiomet/biometric-service-api-portal) provides a pluggable model for biometric sensors to integrate with Windows 10. A fingerprint sensor that plugs into WBF will be exposed to the user as a part of Windows Hello. Fingerprint sensors can register with the framework by implementing a user mode driver that works with the [Windows Biometric Driver Interface (WBDI)](../biometric/index.md). Adapters included in the driver allow WBF to call into the sensor to orchestrate biometric operations, including capturing samples, matching operations, and template management operations.