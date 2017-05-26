---
title: Processing the D3DDP2OP\_CLEAR DP2 Token
description: Processing the D3DDP2OP\_CLEAR DP2 Token
ms.assetid: ec027f44-bdd5-4d5a-8c47-1ac6a0c1cb6e
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , pure devices, D3DDP2OP_CLEAR DP2 token processing
- pure devices WDK DirectX 8.0 , D3DDP2OP_CLEAR DP2 token processing
- D3DDP2OP_CLEAR WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing the D3DDP2OP\_CLEAR DP2 Token


## <span id="ddk_processing_the_d3ddp2op_clear_dp2_token_gg"></span><span id="DDK_PROCESSING_THE_D3DDP2OP_CLEAR_DP2_TOKEN_GG"></span>


DirectX 8.0 introduces some changes to the required processing of the D3DDP2OP\_CLEAR token. Specifically a new flag D3DCLEAR\_COMPUTERECTS has been added to the **dwFlags** field of the [**D3DHAL\_DP2CLEAR**](https://msdn.microsoft.com/library/windows/hardware/ff545441) data structure. This new flag is only passed to the driver when a pure device type is being used (that is, D3DCREATE\_PUREDEVICE was specified when creating the device and the driver exports the D3DDEVCAPS\_PUREDEVICE device cap). Furthermore, this flag is never passed to non-DirectX 8.0 drivers and it is not specified by using the legacy **Clear** or **Clear2** driver callbacks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20the%20D3DDP2OP_CLEAR%20DP2%20Token%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




