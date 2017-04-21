---
title: Sample Interface for UVC Extension Units
author: windows-driver-content
description: Sample Interface for UVC Extension Units
ms.assetid: 898fdaf7-c3e1-4ef5-be4e-a5f9849ee905
keywords:
- interfaces WDK USB Video Class
- extension units WDK USB Video Class , samples, interface
- sample code WDK USB Video Class , interface for UVC extension units
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sample Interface for UVC Extension Units


This topic contains code for a sample *interface.idl* that you can use to support Extension Units.

```
// IExtensionUnit interface
import "unknwn.idl";
[
   object,
   local,
   uuid(yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy),
   pointer_default(unique)
]
interface IExtensionUnit : IUnknown
{
   HRESULT get_InfoSize(
      [out] ULONG *pulSize);
   HRESULT get_Info(
      [in] ULONG ulSize,
      [in, out, size_is(ulSize)] BYTE pInfo[]);
   HRESULT get_PropertySize(
      [in] ULONG PropertyId,
      [out] ULONG *pulSize);
 HRESULT get_Property(
      [in] ULONG PropertyId,
      [in] ULONG ulSize,
      [in, out, size_is(ulSize)] BYTE pValue[]);
   HRESULT put_Property(
      [in] ULONG PropertyId,
      [in] ULONG ulSize,
      [in, out, size_is(ulSize)] BYTE pValue[]);
   HRESULT get_PropertyRange(
      [in] ULONG PropertyId,
      [in] ULONG ulSize,
      [in, out, size_is(ulSize)] BYTE pMin[],
      [in, out, size_is(ulSize)] BYTE pMax[],
      [in, out, size_is(ulSize)] BYTE pSteppingDelta[],
      [in, out, size_is(ulSize)] BYTE pDefault[]);
};
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Sample%20Interface%20for%20UVC%20Extension%20Units%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


