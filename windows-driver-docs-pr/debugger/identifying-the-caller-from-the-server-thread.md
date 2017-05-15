---
title: Identifying the Caller From the Server Thread
description: Identifying the Caller From the Server Thread
ms.assetid: d19dc242-1043-4e61-9fcb-eadac0ab63c8
keywords: ["RPC debugging, identifying the caller"]
---

# Identifying the Caller From the Server Thread


## <span id="ddk_identifying_the_caller_from_the_server_thread_dbg"></span><span id="DDK_IDENTIFYING_THE_CALLER_FROM_THE_SERVER_THREAD_DBG"></span>


It is possible to determine what made a given RPC call, even if the only information you have is the server thread that serviced the call.

This can be very useful -- for example, to find out who passed invalid parameters to an RPC call.

Depending on which protocol sequence is used by this particular call, you can get varying degrees of detail. Some protocols (such as NetBios) do not have this information at all.

**Identifying the caller from the server thread**

1.  Start a user-mode debugger with the server thread as the target.

2.  Get the process ID by using the [**| (Process Status)**](---process-status-.md) command:
    ```
    0:001> |
      0     id: 3d4 name: rtsvr.exe
    ```

3.  Get the active calls in this process by using the [**!rpcexts.getcallinfo**](-rpcexts-getcallinfo.md) extension. (See the reference page for an explanation of the syntax.) You need to supply the process ID of 0x3D4:

    ```
    0:001> !rpcexts.getcallinfo 0 0 FFFF 3d4
    Searching for call info ...
    PID  CELL ID   ST PNO IFSTART  THRDCELL  CALLFLAG CALLID   LASTTIME CONN/CLN
    ----------------------------------------------------------------------------
    03d4 0000.0004 02 000 19bb5061 0000.0002 00000001 00000001 00a1aced 0000.0003
    ```

    Look for calls with status 02 or 01 (dispatched or active). In this example, the process only has one call. If there were more, you would have to use the [**!rpcexts.getdbgcell**](-rpcexts-getdbgcell.md) extension with the cell number in the THRDCELL column. This would allow you to examine the thread IDs so you could determine which call you were interested in.

4.  After you know which call you are interested in, look at the cell number in the CONN/CLN column. This is the cell ID of the connection object. In this case, the cell number is 0000.0003. Pass this cell number and the process ID to **!rpcexts.getdbgcell**:
    ```
    0:001> !rpcexts.getdbgcell 3d4 0.3
    Getting cell info ...
    Connection
    Connection flags: Exclusive
    Authentication Level: Default
    Authentication Service: None
    Last Transmit Fragment Size: 24 (0x6F56D)
    Endpoint for the connection: 0x0.1
    Last send time (in seconds since boot):10595.565 (0x2963.235)
    Last receive time (in seconds since boot):10595.565 (0x2963.235)
    Getting endpoint info ...
    Process object for caller is 0xFF9DF5F0
    ```

This extension will display all the information available about the client of this connection. The amount of actual information will vary, depending on the transport being used.

In this example, local named pipes are being used as the transport and the process object address of the caller is displayed. If you attach a kernel debugger (or start a local kernel debugger), you can use the [**!process**](-process.md) extension to interpret this process address.

If LRPC is used as the transport, the process ID and thread ID of the caller will be displayed.

If TCP is used as the transport, the IP address of the caller will be displayed.

If remote named pipes are used as the transport, no information will be available.

**Note**   The previous example shows how to find the client thread if you know the server thread. For an example of the reverse technique, see [Analyzing a Stuck Call Problem](analyzing-a-stuck-call-problem.md).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Identifying%20the%20Caller%20From%20the%20Server%20Thread%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




