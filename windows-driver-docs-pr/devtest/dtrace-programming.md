---
title: DTrace Programming
description: DTrace supports the D programing language. This topic provide D code samples.
keywords:
- DTrace WDK
- software tracing WDK , DTrace
- displaying trace messages
- formatting trace messages WDK DTrace
- trace message formatting WDK DTrace
- software tracing WDK , formatting messages
- tracing WDK , DTrace
- trace message format files WDK
ms.date: 11/04/2019
---

# DTrace Programming

DTrace supports the D programing language. This topic describes how to get started writing and using DTrace scripts.

For general information about DTrace on Windows, see [DTrace](dtrace.md).

For detailed information about DTrace see the [OpenDTrace Speciﬁcation version 1.0](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-924.pdf) at the University Of Cambridge.

> [!NOTE]
> DTrace is supported in the Insider builds of Windows after version 18980 and Windows Server Insider Preview Build 18975.

## Additional sample scripts

Additional D scripts applicable for Windows scenarios are available in the samples directory of the DTrace source code.

[https://github.com/microsoft/DTrace-on-Windows/tree/master/samples/windows](https://github.com/microsoft/DTrace-on-Windows/tree/master/samples/windows)

A set of opentrace toolkit scripts is available at [https://github.com/opendtrace/toolkit](https://github.com/opendtrace/toolkit).


## Hello World

DTrace scripts are simple text files that contain commands and D programming script elements.

```dtrace
dtrace:::BEGIN
{
  trace("Hello World from DTrace!");
  exit(0);
}
```

Save the file as helloworld.d.

Open a command prompt window as an Administrator and run the script using the -s option.

```dtrace
dtrace -s helloworld.d
dtrace: script '.\helloworld.d' matched 1 probe
CPU     ID                    FUNCTION:NAME
  0      1                           :BEGIN   Hello World from DTrace!
```

## NtCreateUserProcess return time

You can author DTrace scripts to track time taken across multiple functions/events. Below is a simple example that tracks the NtCreateUserProcess function between entry/return for the create process.

```dtrace

syscall::NtCreateUserProcess:entry
{
    self->ts = timestamp;
}

syscall::NtCreateUserProcess:return
{
    printf(" [Caller %s]: Time taken to return from create process is %d MicroSecond \n", execname, (timestamp - self->ts)/ 1000);
}

```

Save the file as ntcreatetime.d and use the -s option to run the test script.


```dtrace
C:\Windows\system32>dtrace -s ntcreatetime.d
dtrace: script 'ntcreatetime.d' matched 2 probes
CPU     ID                    FUNCTION:NAME
  0    183       NtCreateUserProcess:return  [Caller svchost.exe]: Time taken to return from create process is 51191 MicroSecond

  0    183       NtCreateUserProcess:return  [Caller SearchIndexer.]: Time taken to return from create process is 84418 MicroSecond

  0    183       NtCreateUserProcess:return  [Caller SearchIndexer.]: Time taken to return from create process is 137961 MicroSecond

```

## File Delete Tracker

This sample script uses syscall provider to instrument NtOpenFile on entry and checks for flag passed (argument #5) to track deletes across the system.

Copy the below script into filedeletetracker.d.

```dtrace
ERROR{exit(0);}

struct ustr{uint16_t buffer[256];};

syscall::NtOpenFile:entry
{
   this->deleted = arg5 & 0x00001000; /* & with FILE_DELETE_ON_CLOSE */

  if (this->deleted) {
        this->attr = (nt`_OBJECT_ATTRIBUTES*)
            copyin(arg2, sizeof(nt`_OBJECT_ATTRIBUTES));

        if (this->attr->ObjectName) {
            this->objectName = (nt`_UNICODE_STRING*)
                copyin((uintptr_t)this->attr->ObjectName,
                       sizeof(nt`_UNICODE_STRING));
          
            this->fname = (uint16_t*)
                copyin((uintptr_t)this->objectName->Buffer,
                       this->objectName->Length);

            printf("Process %s PID %d deleted file %*ws \n", execname,pid, 
			this->objectName->Length / 2, 
			 ((struct ustr*)this->fname)->buffer);
        }
    }
}
```

Use the -s option to run the test script.

Create or locate a file that you would like to delete. Move the file to the Recycle Bin and then empty the Recycle Bin. When the file is deleted and event will fire and the information about the file delete will be displayed.

```dtrace
C:\Windows\system32>dtrace -s filedeletetracker.d
dtrace: script 'filedeletetracker.d' matched 8 probes
CPU     ID                    FUNCTION:NAME
  0    512                 NtOpenFile:entry Process explorer.exe PID 4684 deleted file \??\C:\$Recycle.Bin\S-1-12-1-3310478672-1302480547-4207937687-2985363607\$ROSR3FA.txt
```

This program is designed to continue to monitor file deletes. Press CTRL+C to exit.

For additional larger code samples, see the next topic, [DTrace Windows Code Samples](dtrace-code-samples.md).

## See Also

[DTrace on Windows](dtrace.md)

[DTrace ETW](dtrace-etw.md)

[DTrace Windows Code Samples](dtrace-code-samples.md)

[DTrace Live Dump](dtrace-live-dump.md)
