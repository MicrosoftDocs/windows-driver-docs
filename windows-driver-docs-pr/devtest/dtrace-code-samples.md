---
title: DTrace Code Samples 
description: Learn about DTrace, which supports the D programing language. See code samples and view additional available support.
keywords:
- DTrace WDK
- software tracing WDK , DTrace
- displaying trace messages
- formatting trace messages WDK DTrace
- trace message formatting WDK DTrace
- software tracing WDK , formatting messages
- tracing WDK , DTrace
- trace message format files WDK
ms.date: 05/02/2022
---

# DTrace Code Samples

DTrace supports the D programing language. This topic provide D code samples.

For general information about DTrace on Windows, see [DTrace](dtrace.md).

For detailed information about DTrace see the [OpenDTrace Speciﬁcation version 1.0](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-924.pdf) at the University Of Cambridge.

> [!NOTE]
> DTrace is supported in the Insider builds of Windows after version 18980 and Windows Server Insider Preview Build 18975.

## Additional sample scripts

Additional D scripts applicable for Windows scenarios are available in the samples directory of the DTrace source code.

[https://github.com/microsoft/DTrace-on-Windows/tree/windows/samples/windows](https://github.com/microsoft/DTrace-on-Windows/tree/windows/samples/windows)

A set of useful opentrace toolkit scripts is available at [https://github.com/opendtrace/toolkit](https://github.com/opendtrace/toolkit).


## Disk Usage by Name

This script provides the disk counters for a given executable name. The executable name is case sensitive and is provided on the command line when the script is started.

```dtrace

#pragma D option quiet
#pragma D option destructive


intptr_t curptr;
struct nt`_EPROCESS *eprocess_ptr;
int found;
int firstpass;
BEGIN
{
	curptr = (intptr_t) ((struct nt`_LIST_ENTRY *) (void*)&nt`PsActiveProcessHead)->Flink;	
	found = 0;
	firstpass = 1;
	bytesread = 0;
	byteswrite = 0;
	readcount = 0;
	writecount = 0;
	flushcount = 0;
}

tick-1ms

/found == 0/

{
/* use this for pointer parsing */
	if (found == 0)
	{
		eprocess_ptr = (struct nt`_EPROCESS *)(curptr - offsetof(nt`_EPROCESS, ActiveProcessLinks));
		processid = (string) eprocess_ptr->ImageFileName;

		if ($1 == processid)
		{
			found = 1;
		}

		else 
		{
			curptr = (intptr_t) ((struct nt`_LIST_ENTRY *) (void*)curptr)->Flink;
		}
	}		
}

tick-2s

{
	system ("cls");
	if (found == 1)
	{
		if (firstpass)
		{
			firstpass = 0;
			bytesread = (unsigned long long) eprocess_ptr->DiskCounters->BytesRead;
			byteswrite = (unsigned long long) eprocess_ptr->DiskCounters->BytesWritten;
			readcount = eprocess_ptr->DiskCounters->ReadOperationCount;
			writecount = eprocess_ptr->DiskCounters->WriteOperationCount;
			flushcount =  eprocess_ptr->DiskCounters->FlushOperationCount;
		}

		else
		{
			bytesread = (unsigned long long)  (eprocess_ptr->DiskCounters->BytesRead - bytesread);
			byteswrite = (unsigned long long)  (eprocess_ptr->DiskCounters->BytesWritten - byteswrite);
			readcount = eprocess_ptr->DiskCounters->ReadOperationCount - readcount;
			writecount = eprocess_ptr->DiskCounters->WriteOperationCount - writecount;		
			flushcount = eprocess_ptr->DiskCounters->FlushOperationCount - flushcount;

			printf("*** Reports disk read/write every second *** \n");
			printf("Process name: %s\n", eprocess_ptr->ImageFileName);
			printf("Process Id: %d\n", (int) eprocess_ptr->UniqueProcessId);
			printf("Bytes Read %llu \n",  (unsigned long long) bytesread);
			printf("Bytes Written %llu \n", (unsigned long long) byteswrite);
			printf("Read Operation Count %d \n", readcount);
			printf("Write Operation Count %d \n",writecount);
			printf("Flush Operation Count %d \n", flushcount);

			bytesread = (unsigned long long) eprocess_ptr->DiskCounters->BytesRead;
			byteswrite = (unsigned long long) eprocess_ptr->DiskCounters->BytesWritten;
			readcount = eprocess_ptr->DiskCounters->ReadOperationCount;
			writecount = eprocess_ptr->DiskCounters->WriteOperationCount;
			flushcount =  eprocess_ptr->DiskCounters->FlushOperationCount;		
		}		
	}

	else
	{
		printf("No matching process found for %s \n", $1);
		exit(0);
	}
}
```

Save the file as diskuagebyname.d and use the -s option to run the test script. Provide a case sensitive name of the desired exe such as Notepad.exe

```dtrace

C:\>dtrace -s diskusagebyname.d Notepad.exe

*** Reports disk read/write every second *** 
Process name: Notepad.exe
Process Id: 6012
Bytes Read 0 
Bytes Written 0 
Read Operation Count 0 
Write Operation Count 0 
Flush Operation Count 0 
*** Reports disk read/write every second *** 
Process name: cmd.exe
Process Id: 4428
Bytes Read 18446744073709480960 
Bytes Written 18446744073709522944 
Read Operation Count -5 
Write Operation Count -7 
Flush Operation Count 0 

```

To keep a running log of disk activity redirect the command out to a text file as shown here.

```dtrace
C:\>dtrace -s diskusagebyname.d Notepad.exe>>diskstats.txt
```

## Dumping Memory Usage

In some diagnostics cases, there is a need to dump kernel structures to understand the situation. This code shows an example to dump system memory usage. The below D-script fires a timer probe every 3 second and refreshes system memory usage.

```dtrace
#pragma D option quiet
#pragma D option destructive

tick-3s
{
	system ("cls");

	this->pp = ((struct nt`_MI_PARTITION *) &nt`MiSystemPartition);

	printf("***** Printing System wide page information ******* \n");
	printf( "Total Pages Entire Node: %u MB \n", this->pp->Core.NodeInformation->TotalPagesEntireNode*4096/(1024*1024));
	printf("Total Available Pages: %u Mb \n", this->pp->Vp.AvailablePages*4096/(1024*1024));
	printf("Total ResAvail Pages: %u  Mb \n",  this->pp->Vp.ResidentAvailablePages*4096/(1024*1024));
	printf("Total Shared Commit: %u  Mb \n",  this->pp->Vp.SharedCommit*4096/(1024*1024));
	printf("Total Pages for PagingFile: %u  Mb \n",  this->pp->Vp.TotalPagesForPagingFile*4096/(1024*1024));
	printf("Modified Pages : %u  Mb \n",  this->pp->Vp.ModifiedPageListHead.Total*4096/(1024*1024));
	printf("Modified No Write Page Count : %u  Mb \n",  this->pp->Vp.ModifiedNoWritePageListHead.Total*4096/(1024*1024));
	printf("Bad Page Count : %d  Mb \n",  this->pp->PageLists.BadPageListHead.Total*4096/(1024*1024));
	printf("Zero Page Count : %d  Mb \n",  this->pp->PageLists.ZeroedPageListHead.Total*4096/(1024*1024));
	printf("Free Page Count : %d  Mb \n",  this->pp->PageLists.FreePageListHead.Total*4096/(1024*1024));


/********** Printing Commit info ******************/ 
	
	this->commit = ((struct nt`_MI_PARTITION_COMMIT ) ((struct nt`_MI_PARTITION *) &nt`MiSystemPartition)->Commit);

	printf("***** Printing Commit Info ******* \n");
	printf("Total Committed Pages: %u  Mb \n", this->pp->Vp.TotalCommittedPages*4096/(1024*1024));
	printf("Total Commit limit: %u  Mb  \n", this->pp->Vp.TotalCommitLimit*4096/(1024*1024));
	printf("Peak Commitment: %u Mb \n", this->commit.PeakCommitment*4096/(1024*1024));
	printf("Low Commit Threshold: %u Mb \n", this->commit.LowCommitThreshold*4096/(1024*1024));
	printf("High Commit Threshold: %u Mb \n", this->commit.HighCommitThreshold*4096/(1024*1024));
	printf("System Commit Reserve: %u Mb \n", this->commit.SystemCommitReserve*4096/(1024*1024));
	

}
```

Save the file as dumpmemoryusage.d.

This sample uses symbols, so set the symbol path as discussed in installation.

```cmd
set _NT_SYMBOL_PATH=srv*C:\symbols*https://msdl.microsoft.com/download/symbols 
```
Use the -s option to run the test script.

```dtrace
C:\>dtrace -s dumpmemoryusage.d
***** Printing System wide page information ******* 
Total Pages Entire Node: 2823 MB 
Total Available Pages: 622 Mb 
Total ResAvail Pages: 2369  Mb 
Total Shared Commit: 166  Mb 
Total Pages for PagingFile: 30  Mb 
Modified Pages : 30  Mb 
Modified No Write Page Count : 0  Mb 
Bad Page Count : 0  Mb 
Zero Page Count : 7  Mb 
Free Page Count : 0  Mb 
***** Printing Commit Info ******* 
Total Committed Pages: 2401  Mb 
Total Commit limit: 4551  Mb  
Peak Commitment: 2989 Mb 
Low Commit Threshold: 3413 Mb 
High Commit Threshold: 4295 Mb 
System Commit Reserve: 5 Mb 
```

This program is designed to continue to monitor memory usage. Press CTRL+C to exit.

## Identifying heap free time breakdown for an activity

This sample provides a breakdown of the  [RtlFreeHeap](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtlfreeheap) function into sub-functions and display max time taken for these functions to execute.

```dtrace
/* Mark script destructive as we call "cls" in the tick-1sec provider*/
#pragma D option destructive

/* Program to calculate time taken in RtlFreeHeap function. Hit Ctrl-C to break. */ 

dtrace:::BEGIN 
{
	counter1 = 0;

}

tick-1sec
{
	system ("cls");
	printf("count of function hit = %d << Press Ctrl-C to exit >> \n", counter1);

}

/* Instrument entry of RtlFreeHeap*/

pid$1:ntdll:RtlFreeHeap:entry
{ 
	/* self is thread local */
	self->ts = timestamp;
	self->depth = 0;
	counter1++;
} 

pid$1:ntdll:RtlFreeHeap:return
/self->ts/
{
	this->ts = timestamp - self->ts;
	@disttime = quantize(this->ts); 
	@funcName[probemod,probefunc] = max(this->ts);	
	self->ts = 0;
}


pid$1:::entry
/ self->ts /
{
	self->functime[self->depth] = timestamp;
	self->depth++;
}

pid$1:::return
/ self->ts /
{
	if (self->depth > 0)
	{
		self->depth--;
		/* this is a local scope */
		this->ts = timestamp - self->functime[self->depth];
		@funcName[probemod,probefunc] = max(this->ts);
	}
}

END

{
	system ("cls");
	/* Print overall time distribution for RtlFreeHeap */
	printa (@disttime);
	/* Print top 15 functions along with average time spent executing them */
	trunc (@funcName, 15);
	
	printa( @funcName);
	
}

```

Save the file as heapfree.d.

This script takes a process ID or PID. To test the script, run tasklist at the command prompt and locate the desired PID.

```dtrace
C:\>tasklist

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0        108 K
Registry                        72 Services                   0     35,576 K

...

Notepad.exe                   7944 31C5CE94259D4006           2     20,736 K

```

Specify the PID as a parameter and use the -s option to run the test script as shown.

```dtrace
C:\>dtrace -s heapfree.d 7944

count of function hit = 28 <<Press Ctrl-C to exit>>
```

Perform what ever task is of interest in the program associated with the PID, for example typing in Notepad or changing the font.

Press CRTL-C and the heap usage will be displayed along with stack information.

```dtrace
           value  ------------- Distribution ------------- count
            4096 |                                         0
            8192 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        23
           16384 |@@@@@@                                   4
           32768 |                                         0
           65536 |                                         0
          131072 |@                                        1
          262144 |                                         0


  ntdll                                               RtlTryEnterCriticalSection                                     9444
  ntdll                                               RtlGetCurrentServiceSessionId                                 12302
  ntdll                                               RtlFreeHeap                                                  151354
  ```

## Memory Pool Tracking

Note: Run this script with aggsortkeypos variable set. This variable informs D-Trace to sort the output based on first index (size).

Usage:

`dtrace -s <script.d>  <Time> <Tag> -x  aggsortkey -x aggsortkeypos=1` 

Example for tracking KSec leaks: dtrace -s PoolTrackingSummary.d "120s" 0x6365734b -x aggsortkey -x aggsortkeypos=1 

The `<Tag>` value is an encoded ASCII value of the memory pool tag. For example to encode the tag value for the nt file system - NtFf, first reverse the two sets of letters, it will be fFtN. Converting the ASCII characters to hex will be 46 66 74 4e, or 0x4666744e as a parameter to our program.

Another example would be converting Ksec.

First reverse the order of the letters: cesK

Then convert those characters to hex, 63 65 73 4b or 0x6365734b as a parameter to our program.

Note that upper lower case is important to match the pool tag.

Output: The script runs for 120 seconds and outputs the KSec allocation/free summary. You can set this to whatever time is necessary.

```dtrace
#pragma D option destructive
#pragma D option quiet
#pragma D option dynvarsize=240m 
#pragma D option bufsize=120m
#pragma D option aggsize=120m 


fbt:nt:ExAllocatePoolWithTag:entry
{	
    /* This is E100 in reserve. Convert ASCII to Hex => Hex('001E').*/
    if (arg2 == $2) 
    { 
		self->size = (unsigned int) arg1;
		@allocstack[stack(), self->size] = count();
    }
}

fbt:nt:ExAllocatePoolWithTag:return
/self->size/
{
    @mem[(uintptr_t) arg1] = sum(1);
    addr[(uintptr_t) arg1] = 1;
    /* printf("%Y: Execname %s allocated size %d bytes return ptr %x", walltimestamp, execname, (uint64_t) self->size, (uintptr_t) arg1 );*/

    size[(uintptr_t) arg1] = self->size;
    @sizealloc[self->size] = count();
    @delta[self->size] = sum(1);
    
    self->size = 0;
}

fbt:nt:ExFreePoolWithTag:entry
/addr[(uintptr_t) arg0]/
{
    @mem[(uintptr_t) arg0] = sum (-1);
    addr[(uintptr_t) arg0] -= 1;

    @sizefree[size[(uintptr_t) arg0]] = count();
    @delta[size[(uintptr_t) arg0]] = sum(-1);
}

tick-$1
{	
    exit(0);
}

END 
{

   printf("%10s %10s %10s %10s\n", "SIZE", "ALLOC", "FREE", "DELTA");
   printa("%10d %@10d %@10d %@10d\n", @sizealloc, @sizefree, @delta);

   printf("Printing stacks \n");
   printa (@allocstack);
    
   printf("== REPORT ==\n\n");
   printa("0x%x => %@u\n",@mem);
}

```

Save the file as pooltrackingsummary.d and use the -s option to run the test script, providing a tag value and other parameters discussed above.

The 120s option, the program runs for two minutes. During that time, use Windows to exercise the monitored memory pool. For example load and unload a web browser or other programs.

```dtrace
C:\>dtrace -s pooltrackingsummary.d "120s" 0x4666744e -x aggsortkey -x aggsortkeypos=1
      SIZE      ALLOC       FREE      DELTA
      1552         16          0         16
Printing stacks

              Ntfs.sys`NtfsCreateFcb+0x388
              Ntfs.sys`NtfsCreateNewFile+0xaa8
              Ntfs.sys`NtfsCommonCreate+0x2303
              Ntfs.sys`NtfsFsdCreate+0x284
              nt`IofCallDriver+0x55
              FLTMGR.SYS`FltpLegacyProcessingAfterPreCallbacksCompleted+0x1b9
              FLTMGR.SYS`FltpCreate+0x324
              nt`IofCallDriver+0x55
              nt`IoCallDriverWithTracing+0x34
              nt`IopParseDevice+0x6ac
              nt`ObpLookupObjectName+0x3fe
              nt`ObOpenObjectByNameEx+0x1fa
              nt`IopCreateFile+0x40f
              nt`NtCreateFile+0x79
              nt`KiSystemServiceCopyEnd+0x38
     1552                3

              Ntfs.sys`NtfsCreateFcb+0x388
              Ntfs.sys`NtfsOpenFile+0x2d7
              Ntfs.sys`NtfsCommonCreate+0x25a8
              Ntfs.sys`NtfsFsdCreate+0x284
              nt`IofCallDriver+0x55
              FLTMGR.SYS`FltpLegacyProcessingAfterPreCallbacksCompleted+0x1b9
              FLTMGR.SYS`FltpCreate+0x324
              nt`IofCallDriver+0x55
              nt`IoCallDriverWithTracing+0x34
              nt`IopParseDevice+0x6ac
              nt`ObpLookupObjectName+0x3fe
              nt`ObOpenObjectByNameEx+0x1fa
              nt`IopCreateFile+0x40f
              nt`NtCreateFile+0x79
              nt`KiSystemServiceCopyEnd+0x38
     1552                4

              Ntfs.sys`NtfsCreateFcb+0x388
              Ntfs.sys`NtfsOpenFile+0x2d7
              Ntfs.sys`NtfsCommonCreate+0x25a8
              Ntfs.sys`NtfsFsdCreate+0x284
              nt`IofCallDriver+0x55
              FLTMGR.SYS`FltpLegacyProcessingAfterPreCallbacksCompleted+0x1b9
              FLTMGR.SYS`FltpCreate+0x324
              nt`IofCallDriver+0x55
              nt`IoCallDriverWithTracing+0x34
              nt`IopParseDevice+0x6ac
              nt`ObpLookupObjectName+0x3fe
              nt`ObOpenObjectByNameEx+0x1fa
              nt`IopCreateFile+0x40f
              nt`NtOpenFile+0x58
              nt`KiSystemServiceCopyEnd+0x38
     1552                3

...

== REPORT ==

0xffffd304c98dd380 => 1
0xffffd304cc4655a0 => 1
0xffffd304cccf15a0 => 1
0xffffd304ccdeb990 => 1
0xffffd304ce048760 => 1
0xffffd304cf1ee990 => 1
0xffffd304d0473010 => 1
0xffffd304d12075a0 => 1
0xffffd304d14135a0 => 1
0xffffd304d1674010 => 1
0xffffd304d33b3660 => 1
0xffffd304d3b29010 => 1
0xffffd304d42c6010 => 1
0xffffd304d48b2010 => 1
0xffffd304de1fa5f0 => 1
0xffffd304e1ad56a0 => 1
```

## Comparing GUIDs

Although, DTrace does not support GUID's natively, you can create struct as show in this sample code to work with them. Here is a sample of how you can compare GUIDs.

```dtrace
nt`_GUID guidcmp;


/* Sleep After GUID: 29f6c1db-86da-48c5-9fdb-f2b67b1f44da */
dtrace:::BEGIN
{
    printf("Begin\n");
    guidcmp.Data1 = 0x29f6c1db;
    guidcmp.Data2 = 0x86da;
    guidcmp.Data3 = 0x48c5;
    guidcmp.Data4[0] = 0x9f;
    guidcmp.Data4[1]  = 0xdb;
    guidcmp.Data4[2]  = 0xf2;
    guidcmp.Data4[3]  = 0xb6;
    guidcmp.Data4[4]  = 0x7b;
    guidcmp.Data4[5]  = 0x1f;
    guidcmp.Data4[6]  = 0x44;
    guidcmp.Data4[7]  = 0xda;
}

pid$target:PowrProf:PowerReadACValueIndexEx:entry 
{ 
	cidstr = (nt`_GUID *) (copyin(arg2, sizeof(nt`_GUID))); 

	printf("\nPrinting GUID to compare\n");
	print(guidcmp);

	printf("\nPrinting GUID received \n");
	print(*cidstr);

	if ( 	(cidstr->Data1 == guidcmp.Data1) &&
		(cidstr->Data2 == guidcmp.Data2) &&
		(cidstr->Data3 == guidcmp.Data3) &&
		(cidstr->Data4[0] == guidcmp.Data4[0]) &&
		(cidstr->Data4[1] == guidcmp.Data4[1]) &&
		(cidstr->Data4[2] == guidcmp.Data4[2]) &&
		(cidstr->Data4[3] == guidcmp.Data4[3]) &&
		(cidstr->Data4[4] == guidcmp.Data4[4]) &&
		(cidstr->Data4[5] == guidcmp.Data4[5]) &&
		(cidstr->Data4[6] == guidcmp.Data4[6]) &&
		(cidstr->Data4[7] == guidcmp.Data4[7])	)
	{
		printf("GUID matched \n");
	}
	else
	{
		printf("No match");
	}
}

dtrace:::END
{
    printf("End\n");
}
```

Save the file as comparequid.d and use the -s option to run the test script, providing the paramter shown below.

```dtrace
C:\Windows\system32>dtrace -s compareguid.d -c "powercfg /qh scheme_current sub_sleep standbyidle"
dtrace: script 'compareguid.d' matched 9 probes
CPU     ID                    FUNCTION:NAME
  0      1                           :BEGIN Begin
 
Power Scheme GUID: 381b4222-f694-41f0-9685-ff5bb260df2e  (Balanced)
  GUID Alias: SCHEME_BALANCED
  Subgroup GUID: 238c9fa8-0aad-41ed-83f4-97be242c8f20  (Sleep)
    GUID Alias: SUB_SLEEP
    Power Setting GUID: 29f6c1db-86da-48c5-9fdb-f2b67b1f44da  (Sleep after)
      GUID Alias: STANDBYIDLE
      Minimum Possible Setting: 0x00000000
      Maximum Possible Setting: 0xffffffff
      Possible Settings increment: 0x00000001
      Possible Settings units: Seconds
    Current AC Power Setting Index: 0x00000708
   Current DC Power Setting Index: 0x00000384
 
dtrace: pid 7560 has exited
  0  42695    PowerReadACValueIndexEx:entry
Printing GUID to compare
struct _GUID {
    UInt32 Data1 = 0x29f6c1db
    UInt16 Data2 = 0x86da
    UInt16 Data3 = 0x48c5
    UInt8 [8] Data4 = [ 0x9f, 0xdb, 0xf2, 0xb6, 0x7b, 0x1f, 0x44, 0xda ]
}
Printing GUID received
struct _GUID {
    UInt32 Data1 = 0x29f6c1db
    UInt16 Data2 = 0x86da
    UInt16 Data3 = 0x48c5
    UInt8 [8] Data4 = [ 0x9f, 0xdb, 0xf2, 0xb6, 0x7b, 0x1f, 0x44, 0xda ]
}
  0  42695    PowerReadACValueIndexEx:entry GUID matched
```

## See Also

[DTrace on Windows](dtrace.md)

[DTrace Windows Programming](dtrace-programming.md)

[DTrace ETW](dtrace-etw.md)

[DTrace Live Dump](dtrace-live-dump.md)
