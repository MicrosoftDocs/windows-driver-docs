---
title: EXT\_TDOP\_RELEASE
description: The EXT\_TDOP\_RELEASE sub-operation of the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI Request operation releases a typed data description.
ms.assetid: 4c2bbc65-a98d-4ee7-bbd0-e30b33c330e0
keywords: ["EXT_TDOP_RELEASE Windows Debugging"]
topic_type:
- apiref
api_name:
- EXT_TDOP_RELEASE
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EXT\_TDOP\_RELEASE


The EXT\_TDOP\_RELEASE sub-operation of the [**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)[**Request**](request.md) operation releases a typed data description.

**Parameters**

<span id="Operation"></span><span id="operation"></span><span id="OPERATION"></span>**Operation**  
Set to EXT\_TDOP\_RELEASE for this sub-operation.

<span id="InData"></span><span id="indata"></span><span id="INDATA"></span>**InData**  
Specifies the instance of the [**DEBUG\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff541706) structure to release.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
Receives the status code returned by this sub-operation. This is the same as the value returned by [**Request**](request.md).

Remarks
-------

EXT\_TDOP\_RELEASE is a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

The parameters for this sub-operation are members of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure. The members of EXT\_TYPED\_DATA that are not listed in the preceding Parameters section are not used by this sub-operation and should be set to zero. The descriptions of the members in the preceding Parameters section specify only the purpose of the members in this particular setting. See **EXT\_TYPED\_DATA** for more details.

## <span id="see_also"></span>See also


[**DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI**](debug-request-ext-typed-data-ansi.md)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**Request**](request.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20EXT_TDOP_RELEASE%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





