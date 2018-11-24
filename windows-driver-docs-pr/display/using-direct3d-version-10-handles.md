---
title: Using Direct3D Version 10 Handles
description: Using Direct3D Version 10 Handles
ms.assetid: 98cde374-0267-44bc-b285-acf4a6d17ff4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Direct3D Version 10 Handles


Direct3D version 10 handles are strongly typed to prevent misusage and to enable the compiler to detect mismatched handle types. Direct3D version 10 handles have life spans that start with a call to a create-type function (for example, [**CreateGeometryShader**](https://msdn.microsoft.com/library/windows/hardware/ff540648)) and end with a call to a destroy-type function (for example, [**DestroyShader**](https://msdn.microsoft.com/library/windows/hardware/ff552805)). Three categories of handles exist for Direct3D version 10. The first two categories of handles are driver handles, which the Direct3D runtime uses to communicate with the driver, and runtime handles, which the driver uses to communicate with the runtime. The third category of handles are kernel handles. The following sections describe the Direct3D version 10 handles:

[Direct3D Version 10 Runtime and Driver Handles](direct3d-version-10-runtime-and-driver-handles.md)

[Direct3D Version 10 Kernel Handles](direct3d-version-10-kernel-handles.md)

 

 





