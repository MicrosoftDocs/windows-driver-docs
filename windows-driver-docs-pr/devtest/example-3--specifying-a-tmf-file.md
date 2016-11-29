---
title: Example 3 Specifying a TMF File
description: Example 3 Specifying a TMF File
ms.assetid: 202304f0-7f8e-4ad1-b10c-185c33db1498
keywords: ["Tracefmt WDK , TMF files", "TMF files WDK , examples"]
---

# Example 3: Specifying a TMF File


This example demonstrates the methods of specifying the TMF file used to format the trace messages:

-   Use the **-tmf** parameter.

    The following command uses the **-tmf** parameter to specify the path and file name of a TMF file. The path overrides any other TMF path specification.

    ```
    tracefmt mytrace.etl -tmf c:\tracing\37753236-c81f-505e-d40a-128d3bb2b5ff.tmf
    ```

    Tracefmt uses the specified TMF file to format the trace messages in the mytrace.etl file.

-   Use the **-p** parameter.

    The following command uses the **-p** parameter to specify the directory in which the TMF file is located. Tracefmt matches the control GUID of the trace provider with the TMF file name to find the correct TMF file. This saves the user from having to copy or type the cumbersome GUID file name.

    ```
    tracefmt mytrace.etl -p c:\tracing
    ```

    Tracefmt uses the specified TMF file to format the trace messages in the mytrace.etl file.

-   Use %TRACE\_FORMAT\_SEARCH\_PATH%.

    The first command in this series sets the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable to a directory location, in this case, c:\\tracing.

    In the Tracefmt command that follows it, the **-tmf** and **-p** parameters are omitted.

    ```
    set TRACE_FORMAT_SEARCH_PATH=c:\tracing
    tracefmt mytrace.etl
    ```

    Although neither a path nor a directory are specified in the Tracefmt command, Tracefmt searches the c:\\tracing directory for a TMF file, and then uses the content to format the trace messages in the mytrace.etl file.

If the TMF files specified by any of these methods do not include formatting instructions for the trace messages, [TraceView](traceview.md) writes the message to the output file with the "No Format Information found" error message. For example:

```
Unknown( 10): GUID=37753236-c81f-505e-d40a-128d3bb2b5ff (No Format Information found).
Unknown( 11): GUID=37753236-c81f-505e-d40a-128d3bb2b5ff (No Format Information found).
Unknown( 11): GUID=37753236-c81f-505e-d40a-128d3bb2b5ff (No Format Information found).
...
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%203:%20Specifying%20a%20TMF%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




