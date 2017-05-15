---
title: Using Input and Output
description: Using Input and Output
ms.assetid: 7a23ee09-0314-400a-8152-eef49a225427
keywords: ["Debugger Engine, Input and Output", "Input and Output", "Output"]
---

# Using Input and Output


## <span id="ddk_input_and_output_dbx"></span><span id="DDK_INPUT_AND_OUTPUT_DBX"></span>


For an overview of the input and output streams in the debugger engine, see [Input and Output](input-and-output.md).

### <span id="input"></span><span id="INPUT"></span>Input

The engine will ask for input from all its clients if the [**Input**](https://msdn.microsoft.com/library/windows/hardware/ff550962) method is called on a client. The input is returned to the caller of **Input**.

### <span id="input_callbacks"></span><span id="INPUT_CALLBACKS"></span>Input Callbacks

When the engine asks for input from a client, it uses the [IDebugInputCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550785) object registered with that client. An **IDebugInputCallbacks** object may be registered with a client using [*SetInputCallbacks*](https://msdn.microsoft.com/library/windows/hardware/ff556721). Each client can have at most one **IDebugInputCallbacks** object registered with it.

The request for input begins with the engine calling the [**IDebugInputCallbacks::StartInput**](https://msdn.microsoft.com/library/windows/hardware/ff550797) method. This informs the **IDebugInputCallbacks** object that the engine is now waiting for input.

If the **IDebugInputCallbacks** object has some input for the engine, it can call the [**ReturnInput**](https://msdn.microsoft.com/library/windows/hardware/ff554600) method of any client. Once the **ReturnInput** method has been called, the engine will not take any more input. Subsequent callers of this method will be informed that the input was not received.

The engine will then call [**IDebugInputCallbacks::EndInput**](https://msdn.microsoft.com/library/windows/hardware/ff550791) to indicate that it has stopped waiting for input.

Finally, the engine will echo this input to the registered **IDebugOutputCallbacks** object of every client (except the one used to provide the input) by using [**IDebugOutputCallbacks::Output**](https://msdn.microsoft.com/library/windows/hardware/ff550815) with the bit-mask set to DEBUG\_OUTPUT\_PROMPT.

### <span id="output"></span><span id="OUTPUT"></span>Output

Output may be sent to the engine using several client methods -- for example [*Output*](https://msdn.microsoft.com/library/windows/hardware/ff553183) and [*OutputVaList*](https://msdn.microsoft.com/library/windows/hardware/ff553280). Upon receiving output, the engine sends it to some clients.

Clients use an *output mask* to indicate which types of output they are interested in. Whenever output is produced by the engine, it is accompanied by a mask specifying its output type. If the type of output matches the output mask of the client, the client will receive the output. The output mask may be set by calling [**SetOutputMask**](https://msdn.microsoft.com/library/windows/hardware/ff556756) and queried using [**GetOutputMask**](https://msdn.microsoft.com/library/windows/hardware/ff548080). See [**DEBUG\_OUTPUT\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541518) for details of the output mask values.

The list of clients that the engine will send output to is controlled by the *output control*. Typically, the output control is set to send output to all clients; however, it can be temporarily changed using [*ControlledOutput*](https://msdn.microsoft.com/library/windows/hardware/ff539248) and [*ControlledOutputVaList*](https://msdn.microsoft.com/library/windows/hardware/ff539252). See [**DEBUG\_OUTCTL\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541517) for details about output control values.

Output may be buffered by the engine. If multiple pieces of output are passed to the engine, it may collect them and send them to the clients in one large piece. To flush this buffer, use [**FlushCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff545475).

Each client object has an *output width*, which is the width of the output display for the client object. While this width is only used as a hint, some commands and extension functions format their output based on this width. The width is returned by the GetOutputWidth method and can be set using the SetOutputWidth method.

### <span id="output_callbacks"></span><span id="OUTPUT_CALLBACKS"></span>Output Callbacks

When the engine sends output to a client, it uses the [IDebugOutputCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550801) object registered with the client. An **IDebugOutputCallbacks** object may be registered with a client using [*SetOutputCallbacks*](https://msdn.microsoft.com/library/windows/hardware/ff556751). Each client can have at most one **IDebugInputCallbacks** object registered with it.

To send the output, the engine calls the [**IDebugOutputCallbacks::Output**](https://msdn.microsoft.com/library/windows/hardware/ff550815) method.

### <span id="output_line_prefix"></span><span id="OUTPUT_LINE_PREFIX"></span>Output Line Prefix

Each client object has an *output line prefix* which is prepended to every line of output sent to the output callback associated with the client object. This can be used for indentation or to place identifying marks on each line of output.

The output line prefix is returned by GetOutputLinePrefix and can be set using SetOutputLinePrefix. To temporarily change the output line prefix and later change it back again, use PushOutputLinePrefix and PopOutputLinePrefix.

### <span id="log_files"></span><span id="LOG_FILES"></span>Log Files

The debugger engine supports opening a log file to record a debugging session. At most, one log file can be open at a time. Output sent to the output callbacks is also sent to this log file (unless it is flagged to not be logged).

To open a log file, use [**OpenLogFile2**](https://msdn.microsoft.com/library/windows/hardware/ff553155) (or [**OpenLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff553154)). The method [**GetLogFile2**](https://msdn.microsoft.com/library/windows/hardware/ff547025) (or [**GetLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff547016)) returns the currently open log file. To close the log file, use [**CloseLogFile**](https://msdn.microsoft.com/library/windows/hardware/ff539148).

The method [**SetLogMask**](https://msdn.microsoft.com/library/windows/hardware/ff556734) can be used to filter the output sent to the log file, and [**GetLogMask**](https://msdn.microsoft.com/library/windows/hardware/ff547066) will return the current log file filter.

### <span id="prompt"></span><span id="PROMPT"></span>Prompt

In an interactive debugging session, a prompt can be used to indicate to the user that the debugger is waiting for user input. The prompt is sent to the output callbacks using the [*OutputPrompt*](https://msdn.microsoft.com/library/windows/hardware/ff553227) and [*OutputPromptVaList*](https://msdn.microsoft.com/library/windows/hardware/ff553231) methods. The contents of the standard prompt are returned by [**GetPromptText**](https://msdn.microsoft.com/library/windows/hardware/ff548180).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Input%20and%20Output%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




