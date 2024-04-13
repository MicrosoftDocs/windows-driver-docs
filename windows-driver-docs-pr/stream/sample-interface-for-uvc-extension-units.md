---
title: Sample Interface for UVC Extension Units
description: This topic contains code for a sample interface.idl that you can use to support Extension Units.
keywords:
- interfaces WDK USB Video Class
- extension units WDK USB Video Class , samples, interface
- sample code WDK USB Video Class , interface for UVC extension units
ms.date: 09/17/2021
---

# Sample Interface for UVC Extension Units

> [!IMPORTANT]
> The content and sample code in this topic is outdated and currently unsupported. It may not work with the current driver development toolchain.

This topic contains code for a sample *interface.idl* that you can use to support Extension Units.

```IDL
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
