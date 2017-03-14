---
title: Verifying Support of Query Types
description: Verifying Support of Query Types
ms.assetid: 0f925796-d827-42ba-9232-8f221919e6d4
keywords: ["asynchronous query operations WDK DirectX 9.0 , verifying support of query types", "query operations WDK DirectX 9.0 , verifying support of query types", "query types WDK DirectX 9.0"]
---

# Verifying Support of Query Types


## <span id="ddk_verifying_support_of_query_types_gg"></span><span id="DDK_VERIFYING_SUPPORT_OF_QUERY_TYPES_GG"></span>


The DirectX 9.0 runtime must verify which query types that a driver supports before any asynchronous query operations can be performed. To verify the number of query types that the driver supports, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETD3DQUERYCOUNT value. If the driver does not support any query types, it returns zero in the **dwNumQueries** member of the [**DD\_GETD3DQUERYCOUNTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551539) structure for this request.

To receive information about each supported query type, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETD3DQUERY value for each type. The driver then returns information about the query type in a [**DD\_GETD3DQUERYDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551541) structure. For more information about **GetDriverInfo2**, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Verifying%20Support%20of%20Query%20Types%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




