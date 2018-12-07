---
title: FVF Code Changes
description: FVF Code Changes
ms.assetid: d9db4356-570b-4e05-aec9-bf36e26e4570
keywords:
- FVF WDK Direct3D
- multimatrix vertex blending WDK Direct3D , FVF code changes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FVF Code Changes


## <span id="ddk_fvf_code_changes_gg"></span><span id="DDK_FVF_CODE_CHANGES_GG"></span>


The key API impact of multimatrix vertex blending is the addition of the vertex blending weight parameters to the position component of the flexible vertex format (FVF). These parameters are stored as 32-bit IEEE single precision floats. They are indicated as present in the input vertex data by the addition of four new bit patterns for the FVF code: D3DVFV\_XYZB2, D3DVFV\_XYZB3, D3DVFV\_XYZB4, and D3DVFV\_XYZB5.

These codes identify extra DWORDs of space that may alternatively be allocated to other uses, such as particle radius or fog parameter, depending on which features are enabled.

**Note**   If the number of blend weights specified is one less than the number of matrices currently being blended, then the weight assigned to the last matrix is defined to be (1.0 - Bₜ), where Bₜ is the total of the other weights for that vertex.

 

 

 





