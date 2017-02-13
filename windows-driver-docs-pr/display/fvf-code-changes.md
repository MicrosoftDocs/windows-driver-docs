---
title: FVF Code Changes
description: FVF Code Changes
ms.assetid: d9db4356-570b-4e05-aec9-bf36e26e4570
keywords: ["FVF WDK Direct3D", "multimatrix vertex blending WDK Direct3D , FVF code changes"]
---

# FVF Code Changes


## <span id="ddk_fvf_code_changes_gg"></span><span id="DDK_FVF_CODE_CHANGES_GG"></span>


The key API impact of multimatrix vertex blending is the addition of the vertex blending weight parameters to the position component of the flexible vertex format (FVF). These parameters are stored as 32-bit IEEE single precision floats. They are indicated as present in the input vertex data by the addition of four new bit patterns for the FVF code: D3DVFV\_XYZB2, D3DVFV\_XYZB3, D3DVFV\_XYZB4, and D3DVFV\_XYZB5.

These codes identify extra DWORDs of space that may alternatively be allocated to other uses, such as particle radius or fog parameter, depending on which features are enabled.

**Note**   If the number of blend weights specified is one less than the number of matrices currently being blended, then the weight assigned to the last matrix is defined to be (1.0 - Bₜ), where Bₜ is the total of the other weights for that vertex.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20FVF%20Code%20Changes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




