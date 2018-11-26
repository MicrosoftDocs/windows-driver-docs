---
title: TCP chimney offload status indications
description: This topic describes TCP chimney offload status indications 
ms.assetid: 607c9319-82d5-4060-9401-510b7e6e2191
keywords:
- TCP chimney offload status indications, task offload NDIS status indications, TCP chimney offload status indications WDK, TCP chimney offload status indications networking
ms.date: 11/10/2017
ms.localizationpriority: medium
---

# TCP chimney offload status indications

\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target can call the [NdisMIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to request the host stack to:

- Stop offloading state objects to the offload target
- Resume offloading state objects to the offload target
- Terminate the offload of all TCP connections that are offloaded to the offload target

This section includes:

[NDIS_STATUS_OFFLOAD_PAUSE](ndis-status-offload-pause.md) 

[NDIS_STATUS_OFFLOAD_RESUME](ndis-status-offload-resume.md) 

[NDIS_STATUS_UPLOAD_ALL](ndis-status-upload-all.md)

