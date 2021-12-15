---
title: DTrace ETW
description: DTrace supports Event Tracing for Windows (ETW) using the D programing language. 
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

# DTrace ETW

Use DTrace for Windows to process existing ETW events and to add new ETW events.

Event Tracing for Windows (ETW) is an kernel-level tracing facility that lets you log kernel or application-defined events to a log file. You can consume the events in real time or from a log file and use them to debug an application or to determine where performance issues are occurring in the application. For general information about ETW, see [About Event Tracing](/windows/win32/etw/about-event-tracing).

> [!NOTE]
> DTrace is supported in the Insider builds of Windows after version 18980 and Windows Server Insider Preview Build 18975.

For general information about working with DTrace on Windows, see [DTrace](dtrace.md).

## ETW Windows DTrace Provider

You can use DTrace to capture and report trace logged and manifest based ETW events. To probe specific keywords/levels/eventIDs, ETW probes will work much more reliably if you don’t use wild cards. Instead fully specify your probe based on these rules:  

Probename = etw

Modname = Provider guid in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, using all lowercase characters.

Funcname = Level_Keyword of the form 0x00_0x0000000000000000. To match everything this should be set to 0xff_0xffffffffffffffff.

Probename = Integer Event ID or "generic_event" to match all event IDs.

Filtering based on Probename only works for manifested events. Use wild-card (*) for tracelogged events.

The ETW payload is accessed via arg0. This is made up of nt\`\_EVENT\_HEADER followed by event specific date.

### Determining available ETW providers

Use the logman command to display active ETW providers and their Provider GUIDs.

```dtrace
C:\>logman query providers
...
Microsoft-Windows-Kernel-Memory {D1D93EF7-E1F2-4F45-9943-03D245FE6C00}
Microsoft-Windows-Kernel-Network {7DD42A49-5329-4832-8DFD-43D979153A88}
Microsoft-Windows-Kernel-PnP {9C205A39-1250-487D-ABD7-E831C6290539}
Microsoft-Windows-Kernel-Power {331C3B3A-2005-44C2-AC5E-77220C37D6B4}
Microsoft-Windows-Kernel-Prefetch {5322D61A-9EFA-4BC3-A3F9-14BE95C144F8}
Microsoft-Windows-Kernel-Process {22FB2CD6-0E7B-422B-A0C7-2FAD1FD0E716}
...
```

## Displaying existing ETW provider information

DTrace has the capability to output ETW events. This is helpful for scenarios where there is existing ETW pipeline to report, collect and analyze.

Use this example DTrace command to report Microsoft-Windows-Kernel-Memory provider events.

```dtrace
C:\>dtrace -n "etw:d1d93ef7-e1f2-4f45-9943-03d245fe6c00:0xff_0xffffffffffffffff:12"
dtrace: description 'etw:d1d93ef7-e1f2-4f45-9943-03d245fe6c00:0xff_0xffffffffffffffff:12' matched 1 probe
CPU     ID                    FUNCTION:NAME
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
  0   3271       0xff_0xffffffffffffffff:12
```

## Adding new ETW events

Etw trace events can be created by calling the etw\_trace macro. Events will only be logged if there is an active listener for the specified trace provider, otherwise they'll be skipped.

The etw\_trace macro supports basic datatypes such as int8, uint8, int16, uint16, int32, uint32, int64, uint64, hexint32, hexint64 and string. See the *Supported ETW data types* table below for more details.

**Example ETW\_TRACE macro:**

This script generates a custom ETW event when the syscall routine returns 0xc0000001 - STATUS_UNSUCCESSFUL.

You can change the `this->status` value to use a different [NTSTATUS values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) to log different syscall return values.

```dtrace
syscall:::return 
{ 
	this->status = (uint32_t) arg0;

	if (this->status == 0xc0000001UL) 
	{ 
		etw_trace
		(
    		"Tools.DTrace.Platform", /* Provider Name */
   	 		"AAD330CC-4BB9-588A-B252-08276853AF02", /* Provider GUID */
    		"My custom event from DTrace", /* Event Name */
    		1, /* Event Level (0 - 5) */
    		0x0000000000000020, /* Flag */
    		"etw_int32", /* Field_1 Name */
    		"PID",/* Field_1 Type */
     		(int32_t)pid, /* Field_1 Value  */
     		"etw_string", /* Field_2 Name */
     		"Execname", /* Field_2 type */
      		execname, /* Field_2 Value */
     		"etw_string", /* Field_3 Name */
     		"Probefunc", /* Field_3 type */
      		probefunc /* Field_3 Value */   
			);
	}
}
```

```dtrace
C:\> dtrace -s addnewetwevent.d
dtrace: script 'addnewetwevent.d' matched 1881 probes
CPU     ID                    FUNCTION:NAME
  0     93 NtAlpcSendWaitReceivePort:return
  0     93 NtAlpcSendWaitReceivePort:return
  0     93 NtAlpcSendWaitReceivePort:return
```

## ETW NUMA MEM STATS example code

This example script uses Microsoft-Windows-Kernel-Memory ETW provider to dump NUMA node memory. Page size can be converted to size in KB by multiplying by 4. For general information on NUMA see [NUMA Support](/windows/win32/procthread/numa-support).

This code is also located at <https://github.com/microsoft/DTrace-on-Windows/blob/master/samples/windows/etw/numamemstats.d>

```dtrace
typedef struct KernelMemInfoEvent
{
        struct nt`_EVENT_HEADER _EH;
	uint32_t PartitionId;
	uint32_t Count;
	uint32_t NodeNumber;
}kmi;

typedef struct MemoryNodeInfo
{
	uint64_t TotalPageCount;
	uint64_t SmallFreePageCount;
	uint64_t SmallZeroPageCount;
	uint64_t MediumFreePageCount;
	uint64_t MediumZeroPageCount;
	uint64_t LargeFreePageCount;
	uint64_t LargeZeroPageCount;
	uint64_t HugeFreePageCount;
	uint64_t HugeZeroPageCount;
}m_nodeinfo;

int printcounter;

BEGIN
{
	printcounter = 0;
}

/* MemNodeInfo */
etw:d1d93ef7-e1f2-4f45-9943-03d245fe6c00:0xff_0xffffffffffffffff:12
{
	if (printcounter%10 == 0)
	{
		printf ("\n \n");
		printf("Partition ID: %d \n",((kmi *)arg0)->PartitionId);
		printf("Count: %d \n", ((kmi *)arg0)->Count);
		
		printf("Node number: %d\n", ((kmi *)arg0)->NodeNumber);
		counters = (m_nodeinfo*)(arg0 + sizeof(struct nt`_EVENT_HEADER) + 12);
		print(*counters);

		/* Dump rest of the NUMA node info */

		if (((kmi *)arg0)->Count > 1)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(1)) + (sizeof(uint32_t)*(1)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(1)) + (sizeof(uint32_t)*(1)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 2)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(2)) + (sizeof(uint32_t)*(2)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(2)) + (sizeof(uint32_t)*(2)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 3)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(3)) + (sizeof(uint32_t)*(3)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(3)) + (sizeof(uint32_t)*(3)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 4)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(4)) + (sizeof(uint32_t)*(4)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(4)) + (sizeof(uint32_t)*(4)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 5)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(5)) + (sizeof(uint32_t)*(5)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(5)) + (sizeof(uint32_t)*(5)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 6)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(6)) + (sizeof(uint32_t)*(6)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(6)) + (sizeof(uint32_t)*(6)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 7)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(7)) + (sizeof(uint32_t)*(7)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(7)) + (sizeof(uint32_t)*(7)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 8)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(8)) + (sizeof(uint32_t)*(8)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(8)) + (sizeof(uint32_t)*(8)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 9)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(9)) + (sizeof(uint32_t)*(9)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(9)) + (sizeof(uint32_t)*(9)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 10)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(10)) + (sizeof(uint32_t)*(10)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(10)) + (sizeof(uint32_t)*(10)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 11)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(11)) + (sizeof(uint32_t)*(11)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(11)) + (sizeof(uint32_t)*(11)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 12)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(12)) + (sizeof(uint32_t)*(12)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(12)) + (sizeof(uint32_t)*(12)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 13)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(13)) + (sizeof(uint32_t)*(13)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(13)) + (sizeof(uint32_t)*(13)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 14)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(14)) + (sizeof(uint32_t)*(14)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(14)) + (sizeof(uint32_t)*(14)) + sizeof(uint32_t));
			print(*counters);
		}
		if (((kmi *)arg0)->Count > 15)
		{
			nodenumber = (uint32_t *) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(15)) + (sizeof(uint32_t)*(15)) );
			printf ("Node Number: %d \n", *nodenumber);
			counters = (m_nodeinfo*) (arg0 + sizeof(struct nt`_EVENT_HEADER) + 8 + (sizeof(m_nodeinfo)*(15)) + (sizeof(uint32_t)*(15)) + sizeof(uint32_t));
			print(*counters);
		}

	}
	exit(1);
	printcounter++;
}
```

Save the file as etwnumamemstats.d

Open a command prompt as an Administrator and run the script using the -s option. 

Running on a client Windows PC, a single NUMA node is displayed.

```dtrace
C:\> dtrace -s etwnumamemstats.d
trace: script 'etwnumamemstats.d' matched 36 probes
CPU     ID                    FUNCTION:NAME
  0  42735       0xff_0xffffffffffffffff:12

Partition ID: 0
Count: 1
Node number: 1
m_nodeinfo {
    uint64_t TotalPageCount = 0xab98d
    uint64_t SmallFreePageCount = 0
    uint64_t SmallZeroPageCount = 0x1bec
    uint64_t MediumFreePageCount = 0
    uint64_t MediumZeroPageCount = 0x5a
    uint64_t LargeFreePageCount = 0
    uint64_t LargeZeroPageCount = 0
    uint64_t HugeFreePageCount = 0
    uint64_t HugeZeroPageCount = 0
}
  0  42735       0xff_0xffffffffffffffff:12
```

## Supported ETW data types

| **ETW type**           | **D Language data type** | **Notes**                                                                                 |
| ---------------------- | ------------------------ | ----------------------------------------------------------------------------------------- |
| etw\_struct            | Integer                  | The payload value of this type represents the count of member a new structure will have.  |
| etw\_string            | string                   | N/A                                                                                       |
| etw\_mbcsstring        | string                   | N/A                                                                                       |
| etw\_int8              | Integer                  | Type size should match, and casting to \`int8\_t\` in the D script is advised             |
| etw\_uint8             | Integer                  | Type size should match, and casting to \`uint8\_t\` in the D script is advised            |
| etw\_int16             | Integer                  | Type size should match, and casting to \`int16\_t\` in the D script is advised            |
| etw\_uint16            | Integer                  | Type size should match, and casting to \`uint16\_t\` in the D script is advised           |
| etw\_int32             | Integer                  | N/A                                                                                       |
| etw\_uint32            | Integer                  | N/A                                                                                       |
| etw\_int64             | Integer                  | Type must be explicitly be \`int64\_t\` since D defaults to \`int32\_t\`                  |
| etw\_uint64            | Integer                  | Type must be explicitly be \`int64\_t\` since D defaults to \`int32\_t\`                  |
| etw\_float             | Scalar                   | Floating-point constants are not allowed in D script, but does allow it on loaded symbols |
| etw\_double            | Scalar                   | Floating-point constants are not allowed in D script, but does allow it on loaded symbols |
| etw\_bool32            | Integer                  | N/A                                                                                       |
| etw\_hexint32          | Integer                  | N/A                                                                                       |
| etw\_hexint64          | Integer                  | Type must be explicitly be \`int64\_t\` since D defaults to \`int32\_t\`                  |
| etw\_countedmbcsstring | Integer                  | N/A                                                                                       |
| etw\_intptr            | Integer                  | The data type size changes according to the architecture (\`int32\_t\` vs \`int64\_t\`)   |
| etw\_uintptr           | Integer                  | The data type size changes according to the architecture (\`int32\_t\` vs \`int64\_t\`)   |
| etw\_pointer           | Integer                  | The data type size changes according to the architecture (\`int32\_t\` vs \`int64\_t\`)   |
| etw\_char16            | Integer                  | Type size should match, and casting to \`int16\_t\` in the D script is advised            |
| etw\_char8             | Integer                  | Type size should match, and casting to \`int8\_t\` in the D script is advised             |
| etw\_bool8             | Integer                  | Type size should match, and casting to \`int8\_t\` in the D script is advised             |
| etw\_hexint8           | Integer                  | Type size should match, and casting to \`int8\_t\` in the D script is advised             |
| etw\_hexint16          | Integer                  | Type size should match, and casting to \`int16\_t\` in the D script is advised            |
| etw\_pid               | Integer                  | N/A                                                                                       |
| etw\_tid               | Integer                  | N/A                                                                                       |
| etw\_mbcsxml           | Integer                  | N/A                                                                                       |
| etw\_mbcsjson          | Integer                  | N/A                                                                                       |
| etw\_countedmbcsxml    | Integer                  | N/A                                                                                       |
| etw\_countedmbcsjson   | Integer                  | N/A                                                                                       |
| etw\_win32error        | Integer                  | N/A                                                                                       |
| etw\_ntstatus          | Integer                  | N/A                                                                                       |
| etw\_hresult           | Integer                  | N/A                                                                                       |

## See Also

[DTrace on Windows](dtrace.md)

[DTrace Windows Programming](dtrace-programming.md)

[DTrace Windows Code Samples](dtrace-code-samples.md)

[DTrace Live Dump](dtrace-live-dump.md)
