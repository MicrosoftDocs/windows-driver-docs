---
title: Verifying Support of Query Types
description: Verifying Support of Query Types
keywords:
- asynchronous query operations WDK DirectX 9.0 , verifying support of query types
- query operations WDK DirectX 9.0 , verifying support of query types
- query types WDK DirectX 9.0
ms.date: 04/20/2017
---

# Verifying Support of Query Types


## <span id="ddk_verifying_support_of_query_types_gg"></span><span id="DDK_VERIFYING_SUPPORT_OF_QUERY_TYPES_GG"></span>


The DirectX 9.0 runtime must verify which query types that a driver supports before any asynchronous query operations can be performed. To verify the number of query types that the driver supports, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETD3DQUERYCOUNT value. If the driver does not support any query types, it returns zero in the **dwNumQueries** member of the [**DD\_GETD3DQUERYCOUNTDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_getd3dquerycountdata) structure for this request.

To receive information about each supported query type, the runtime sends a **GetDriverInfo2** request using the D3DGDI2\_TYPE\_GETD3DQUERY value for each type. The driver then returns information about the query type in a [**DD\_GETD3DQUERYDATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_dd_getd3dquerydata) structure. For more information about **GetDriverInfo2**, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

 

