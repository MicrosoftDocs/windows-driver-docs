---
title: Managing Resources for Multiple GPU Scenarios
description: Managing Resources for Multiple GPU Scenarios
ms.assetid: f3dc10b1-76e9-4f31-b253-149b6300611d
keywords:
- GPU WDK Windows 7 display
- GPU WDK Windows 7 display , multiple
- GPU WDK Windows 7 display , multiple, managing resources for
- multiple GPUs WDK Windows 7 display
- multiple GPUs WDK Windows 7 display , managing resources for
- GPU WDK Windows 2008 Resource R2 display
- GPU WDK Windows 2008 Resource R2 display , multiple
- GPU WDK Windows 2008 Resource R2 display , multiple, managing resources for
- multiple GPUs WDK Windows 2008 Resource R2 display
- multiple GPUs WDK Windows 2008 Resource R2 display , managing resources for
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Resources for Multiple GPU Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

To appropriately manage resources for multiple GPU scenarios, a user-mode display driver can implement a new device driver interface (DDI) that ships with Windows 7. Each resource might be divided across memory for multiple GPUs to render on. The driver can implement this new DDI to re-merge each resource so that the new resource owner has the merged resource. In this DDI implementation, the driver must flush any partially built command buffers that might modify the resource. This DDI is provided as extensions to the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927) and to the [Direct3D version 10 DXGI DDI](https://msdn.microsoft.com/library/windows/hardware/ff552905). The driver can implement [**ResolveSharedResource**](https://msdn.microsoft.com/library/windows/hardware/ff569487) to support Microsoft Direct3D feature level 9 and [**ResolveSharedResourceDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff569488) to support Direct3D feature levels 10 and 11.

Starting in Windows 8.1, a user-mode driver can support cross-adapter resources that are shared between a discrete GPU and an integrated GPU. See [Using cross-adapter resources in a hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md).

 

 





