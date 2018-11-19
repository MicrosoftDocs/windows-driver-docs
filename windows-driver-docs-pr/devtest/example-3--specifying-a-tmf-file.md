---
title: Example 3 Specifying a TMF File
description: Example 3 Specifying a TMF File
ms.assetid: 202304f0-7f8e-4ad1-b10c-185c33db1498
keywords:
- Tracefmt WDK , TMF files
- TMF files WDK , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





