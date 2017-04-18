---
title: Using Direct3D Version 10 Handles
description: Using Direct3D Version 10 Handles
ms.assetid: 98cde374-0267-44bc-b285-acf4a6d17ff4
---

# Using Direct3D Version 10 Handles


Direct3D version 10 handles are strongly typed to prevent misusage and to enable the compiler to detect mismatched handle types. Direct3D version 10 handles have life spans that start with a call to a create-type function (for example, [**CreateGeometryShader**](https://msdn.microsoft.com/library/windows/hardware/ff540648)) and end with a call to a destroy-type function (for example, [**DestroyShader**](https://msdn.microsoft.com/library/windows/hardware/ff552805)). Three categories of handles exist for Direct3D version 10. The first two categories of handles are driver handles, which the Direct3D runtime uses to communicate with the driver, and runtime handles, which the driver uses to communicate with the runtime. The third category of handles are kernel handles. The following sections describe the Direct3D version 10 handles:

[Direct3D Version 10 Runtime and Driver Handles](direct3d-version-10-runtime-and-driver-handles.md)

[Direct3D Version 10 Kernel Handles](direct3d-version-10-kernel-handles.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Direct3D%20Version%2010%20Handles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




