---
title: Input and Output
description: Input and Output
ms.assetid: 78e181c1-c577-49ca-910b-d2e8db2495b5
keywords: ["Debugger Engine, input and output", "input and output", "output"]
---

# Input and Output


The input and output facilities of the [debugger engine](introduction.md#debugger-engine) can be used for interactive debugger operation and logging. The input usually represents commands and responses that are typed by the user, and the output usually represents information presented to the user or sent to log files.

The debugger engine maintains an *input stream* and an *output stream*. Input can be requested from the input stream, and output sent to the output stream.

When the [**Input**](https://msdn.microsoft.com/library/windows/hardware/ff550962) method is called to request input from the engine's input stream, the engine will call all the registered [input callbacks](using-input-and-output.md#input-callbacks) to inform them that it is waiting for input. It then waits for the input callbacks to provide the input by calling the [**ReturnInput**](https://msdn.microsoft.com/library/windows/hardware/ff554600) method.

When output is sent to the engine's output stream, the engine will call the registered [output callbacks](using-input-and-output.md#output-callbacks) passing the output to them. When sending output to the output stream, it can be filtered by the client object; in which case, only output callbacks that are registered with particular client objects will receive the output.

The input and output streams are transparently available to the remote clients. Remote clients can request input and send output to the engine's input and output stream, and the engine will call the callbacks registered with remote clients to request input or send output.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using input and output, see [Using Input and Output](using-input-and-output.md). For more information about client objects and input and output callbacks, see [Client Objects](client-objects.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Input%20and%20Output%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




