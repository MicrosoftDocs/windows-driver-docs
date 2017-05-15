---
title: Get RPC Client Call Information
description: Get RPC Client Call Information
ms.assetid: 8b23428d-50e7-4613-a0ce-d1da5fa96ddf
keywords: ["RPC client call information", "CCALL (client call)"]
---

# Get RPC Client Call Information


## <span id="ddk_get_rpc_client_call_information_dbg"></span><span id="DDK_GET_RPC_CLIENT_CALL_INFORMATION_DBG"></span>


Client call (CCALL) call information is displayed by the **!rpcexts.getclientcallinfo** extension, or by DbgRpc when the **-a** switch is used.

Four optional parameters are permitted. Three of these -- *CallID*, *IfStart*, and *ProcNum* -- are identifying information used by RPC to keep track of its calls. The fourth parameter, *ProcessID*, is the PID of the process that owns the call. You should supply whatever parameters you know to narrow down the search.

If no parameters are supplied, all known CCALLs in the system will be displayed. The following is an example of this (potentially long) display:

```
D:\wmsg>dbgrpc -a
Searching for call info ...
## PID  CELL ID   PNO  IFSTART  TIDNUMBER CALLID   LASTTIME PS CLTNUMBER ENDPOINT
------------------------------------------------------------------------------
0390 0000.0001 0000 19bb5061 0000.0000 00000001 00072bff 07 0000.0002 1120
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getclientcallinfo**](-rpcexts-getclientcallinfo.md).

**Note**   Information about Client Call objects is only gathered if the **Full** state information is being gathered. See [Enabling RPC State Information](enabling-rpc-state-information.md) for details.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Get%20RPC%20Client%20Call%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




