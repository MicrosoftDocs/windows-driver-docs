---
title: Application Verifier - Stop Codes - Basics 
description: Application Verifier - Stop Codes - Basics 
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/21/2022
---

# Application Verifier - Stop Codes - Basics 

The following stop codes are contained in the basics set of tests.

## Exceptions Stop Details

<h3>Attempt to execute code in non-executable memory (first chance).</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is trying to run code from an address that is non-executable or free. To debug this stop: $ u parameter2 - to unassemble the culprit code $ .exr parameter3 - to display the exception information; $ .cxr parameter4 followed by kb - to display the exception context information and the stack trace for the time when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code performing invalid access.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Exceptions</li>
  <li><b>Stop ID:</b>&nbsp;FIRST_CHANCE_ACCESS_VIOLATION_CODE</li>
  <li><b>Stop code:</b>&nbsp;650NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>

## Handles Stop Details

<h3>Invalid handle exception for current stack trace.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the function on the top of the stack passed an invalid handle to system routines. Usually a simple kb command will reveal what is the value of the handle passed (must be one of the parameters - usually the first one). If the value is null then this is clearly wrong. If the value looks ok you need to use !htrace debugger extension to get a history of operations pertaining to this handle value. In most cases it must be that the handle value is used after being closed.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exception code.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid TLS index used for current stack trace.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the function on the top of the stack passed an invalid TLS index to TLS system routines. Usually a simple kb command will reveal what is wrong. The typical bug here is to assume a certain value for a TLS index instead of calling TlsAlloc. This can happen either by thinking that you always get value N therefore there is no need to call TlsAlloc or more frequently due to an uninitialized variable.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Invalid TLS index.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected lower part of the index.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_TLS_VALUE</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid parameters for WaitForMultipleObjects call.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the function on the top of the stack called WaitForMultipleObjects with NULL as the address of the array of handles to wait for or with zero as the number of handles. A simple kb command will reveal the function calling this API incorrectly.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of object handles vector.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Number of handles.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;INCORRECT_WAIT_CALL</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3> NULL handle passed as parameter. A valid handle must be used. </h3>
<p></p><i>Probable cause</i><p>This stop is generated if the function on the top of the stack passed a NULL handle to system routines.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;NULL_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Waiting on a thread handle in DllMain.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the current thread is currently running code inside the DllMain function of one of the DLLs loaded in the current process and it calls WaitForSingleObject or WaitForMultipleObjects to wait on a thread handle in the same process. This would most likely lead to a deadlock because the thread handle will not get signaled unless that second thread is exiting. When the second thread will call ExitThread it will try to acquire the DLL loader lock then call DllMain (DLL_THREAD_DETACH) for all DLLs in the current process. But the loader lock is owned by the first thread (the one that is waiting on the thread handle) so the two threads will deadlock.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Thread handle.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;WAIT_IN_DLLMAIN</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect object type for handle.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the current thread is calling an API with a handle to an object with an incorrect object type. E.g. calling SetEvent with a semaphore handle as parameter will generate this stop. To debug this stop: $ kb - to display the current stack trace. The culprit is probably the DLL that is calling into verifier.dll; $ du parameter2 - to display the actual type of the handle. The handle value is parameter1. In the example above, this will display: Semaphore. $ du parameter3 - to display the object type expected by the API. In the example above, this name will be: Event. $ !htrace parameter1 might be helpful because it will display the stack trace for the recent open/close operations on this handle.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Handle value.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Object type name. Use du to display it</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected object type name. Use du to display it</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Handles</li>
  <li><b>Stop ID:</b>&nbsp;INCORRECT_OBJECT_TYPE</li>
  <li><b>Stop code:</b>&nbsp;300NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>


## Heaps Stop Details

<h3>Unknown error.</h3>
<p></p><i>Probable cause</i><p>This message can happen if the error encountered cannot be classified in any other way. Not used right now.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;UNKNOWN_ERROR</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Access violation exception.</h3>
<p></p><i>Probable cause</i><p>This is the most common application verifier stop. Typically it is caused by a buffer overrun error. The heap verifier places a non-accessible page at the end of a heap allocation and a buffer overrun will cause an exception by touching this page. To debug this stop identify the access address that caused the exception and then use the following debugger command: !heap -p -a ACCESS_ADDRESS This command will give details about the nature of the error and what heap block is overrun. It will also give the stack trace for the block allocation. There are several other causes for this stop. For example accessing a heap block after being freed. The same debugger command will be useful for this case too.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Invalid address causing the exception</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code address executing the invalid access</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;ACCESS_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Multithreaded access in a heap created with HEAP_NO_SERIALIZE flag.</h3>
<p></p><i>Probable cause</i><p>A heap created with HEAP_NO_SERIALIZE flag is not supposed to be accessed simultaneously from two threads. If such a situation is detected you will get this message. The typical way this situation creeps into a program is by linking with a single-threaded version of the C-runtime. Visual C++ can for instance link statically such a library when proper flags are used. Then people forget about this detail and use multiple threads. The bug is very difficult to debug in real life because it will show up as mysterious data corruptions.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap in which operation happens.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Thread ID for current owner of the heap critical section.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread ID of current thread trying to enter the heap.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;UNSYNCHRONIZED_ACCESS</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Extreme size request.</h3>
<p></p><i>Probable cause</i><p>This message will be generated if in a HeapAlloc() or HeapReAlloc() operation the size of the block is above any reasonable value. Typically this value is 0x80000000 on 32-bit platforms and significantly bigger on 64-bit platforms.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap in which operation happens.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Size requested</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;EXTREME_SIZE_REQUEST</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Heap handle with incorrect signature.</h3>
<p></p><i>Probable cause</i><p>The heap structures are tagged with a magic value. If the heap handle used in the call to a heap interface does not have this pattern then this stop will be generated. This bug can happen if somehow the internal heap structure got corrupted (random corruption) or simply a bogus value is used as a heap handle. To get a list of valid heap handle values use the following debugger commands: !heap -p Note that if you just switch a valid heap handle with another valid one in a heap operation you will not get this stop (the handle looks valid after all). However the heap verifier detects this situation and reports it with SWITCHED_HEAP_HANDLE stop.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call to a heap interface</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;BAD_HEAP_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted heap pointer or using wrong heap.</h3>
<p></p><i>Probable cause</i><p>Typically this happens if a block gets allocated in one heap and freed in another. Use !heap -p command to get a list of all valid heap handle values. The most common example is a msvcrt allocation using malloc() paired with a kernel32 deallocation using HeapFree().</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Heap where block was originally allocated.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;SWITCHED_HEAP_HANDLE</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Heap block already freed.</h3>
<p></p><i>Probable cause</i><p>This situation happens if the block is freed twice. Freed blocks are marked in a special way and are kept around for a while in a delayed free queue. If a buggy program tries to free the block again this will be caught assuming the block was not dequeued from delayed free queue and its memory reused for other allocations. The depth of the delay free queue is in the order of thousands of blocks therefore there are good chances that most double frees will be caught.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle for the heap owning the block.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block being freed again.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;DOUBLE_FREE</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted heap block.</h3>
<p></p><i>Probable cause</i><p>This is a generic error issued if the corruption in the heap block cannot be placed in a more specific category.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Reserved</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to destroy process heap.</h3>
<p></p><i>Probable cause</i><p>It is an error to try to destroy the default process heap (the one returned by GetProcessHeap() interface).</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used with HeapDestroy.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;DESTROY_PROCESS_HEAP</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception raised while executing heap management code.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if while executing the heap manager code an access violation is raised in illegitimate situations. There are very few situations where this is ok, for example when calling HeapValidate() or HeapSize(). The exception record information (third parameter) can be used to find the exact context of the exception. Use the following debugger commands for this: $ .exr STOP-PARAMETER-2 $ .cxr STOP-PARAMETER-3 Usually this stop can happen if there is some random corruption in the internal heap structures.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap involved in the operation.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Exception code (C0000005 - access violation)</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Exception raised while verifying the heap block header.</h3>
<p></p><i>Probable cause</i><p>This situation happens if we really cannot determine any particular type of corruption for the block. Most likely this stop will happen when the heap block address passed to a heap free points to a non-accesible memory area (corrupted pointer, uninitialized pointer, etc.).</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle for the heap owning the block.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block that is corrupted.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the block or zero if size cannot be determined.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_EXCEPTION_RAISED_FOR_HEADER</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Exception raised while verifying the heap block.</h3>
<p></p><i>Probable cause</i><p>This situation happens if we really cannot determine any particular type of corruption for the block. For instance you will get this if during a heap free operation you pass an address that points to a non-accessible memory area. This can also happen for double free situations if we do not find the block among full page heap blocks and we probe it as a light page heap block.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Reserved.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_EXCEPTION_RAISED_FOR_PROBING</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Heap block corrupted after being freed.</h3>
<p></p><i>Probable cause</i><p>This situation happens if a block of memory is written to after being freed.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle for the heap owning the block.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block that is corrupted.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the block or zero if size cannot be determined.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_HEADER</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted infix pattern for freed heap block.</h3>
<p></p><i>Probable cause</i><p>Freed blocks are sometimes marked non-accessible and a program touching them will access violate (different verifier stop). In other cases (light page heap) the block is marked with a magic pattern and will be kept for a while. Eventually in a FIFO fashion the blocks get really freed. At this moment the infix pattern is checked and if it has been modified you will get this break. The stack at the break moment is not relevant. You need to find out the nature of the block and code review the code that might be wrong.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle for the heap owning the block.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block being freed.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Reserved.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_FREED_HEAP_BLOCK</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted suffix pattern for heap block.</h3>
<p></p><i>Probable cause</i><p>Most typically this happens for buffer overrun errors. Sometimes the application verifier places non-accessible pages at the end of the allocation and buffer overruns will cause an access violation and sometimes the heap block is followed by a magic pattern. If this pattern is changed when the block gets freed you will get this break. These breaks can be quite difficult to debug because you do not have the actual moment when corruption happened. You just have access to the free moment (stop happened here) and the allocation stack trace (!heap -p -a HEAP_ADDRESS)</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Reserved.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_SUFFIX</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted start stamp for heap block.</h3>
<p></p><i>Probable cause</i><p>This happens for buffer underruns.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Corrupted stamp value.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_START_STAMP</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted end stamp for heap block.</h3>
<p></p><i>Probable cause</i><p>This happens for buffer underruns.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Corrupted stamp value.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_END_STAMP</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted prefix pattern for heap block.</h3>
<p></p><i>Probable cause</i><p>This happens for buffer underruns.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Heap handle used in the call.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap block involved in the operation.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Size of the heap block.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Reserved.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_BLOCK_PREFIX</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>First chance access violation for current stack trace.</h3>
<p></p><i>Probable cause</i><p>This is the most common application verifier stop. Typically it is caused by a buffer overrun error. The heap verifier places a non-accessible page at the end of a heap allocation and a buffer overrun will cause an exception by touching this page. To debug this stop identify the access address that caused the exception and then use the following debugger command: !heap -p -a ACCESS_ADDRESS This command will give details about the nature of the error and what heap block is overrun. It will also give the stack trace for the block allocation. There are several other causes for this stop. For example accessing a heap block after being freed. The same debugger command will be useful for this case too.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Invalid address causing the exception.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code address executing the invalid access.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;FIRST_CHANCE_ACCESS_VIOLATION</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid process heap list count.</h3>
<p></p><i>Probable cause</i><p>This message can happen if while calling GetProcessHeaps the page heap manager detects some internal inconsistencies. This can be caused by some random corruption in the process space.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Actual heap count.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Page heap count.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Heaps</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_HEAP_LIST</li>
  <li><b>Stop code:</b>&nbsp;0NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>


## Leak Stop Details

<h3>A heap allocation was leaked.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the owner dll of the allocation was dynamically unloaded while owning resources.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the leaked allocation. Run !heap -p -a &lt;address&gt; to get additional information about the allocation.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the allocation stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;ALLOCATION</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A HANDLE was leaked.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the owner dll of the handle was dynamically unloaded while owning resources. To debug this stop: Run !htrace parameter1 to get additional information about the handle.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Value of the leaked handle. Run !htrace &lt;handle&gt; to get additional information about the handle if handle tracing is enabled.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the allocation stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;HANDLE</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>An HKEY was leaked.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the owner dll of the registry key was dynamically unloaded while owning resources.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Value of the leaked HKEY.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the allocation stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;REGISTRY</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A virtual reservation was leaked.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the owner dll of the virtual reservation was dynamically unloaded while owning resources.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Leaked reservation address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the allocation stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;VIRTUAL_RESERVATION</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A BSTR was leaked.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the owner dll of the SysString was dynamically unloaded while owning resources.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the leaked BSTR. Run !heap -p -a &lt;address&gt; to get additional information about the allocation.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the allocation stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;SYSSTRING</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A power notification was not unregistered.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the dll registered for power notification and was dynamically unloaded without unregistering.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the power notification registration.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address to the registration stack trace. Run dps &lt;address&gt; to view the allocation stack.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the owner dll name. Run du &lt;address&gt; to read the dll name.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Base of the owner dll. Run .reload &lt;dll_name&gt; = &lt;address&gt; to reload the owner dll. Use 'lm' to get more information about the loaded and unloaded modules.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Leak</li>
  <li><b>Stop ID:</b>&nbsp;POWER_NOTIFICATION</li>
  <li><b>Stop code:</b>&nbsp;900NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>


## Locks Stop Details

<h3>Thread cannot own a critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a thread (thread ID is parameter1) is terminated, suspended or is in a state (worker thread finished a work item) in which it cannot hold a critical section. The current thread is the culprit. To debug this stop use the following debugger commands: $ kb - to get the current stack trace. If the current thread is the owner of the critical section it is probably calling ExitThread. The current thread should have released the critical section before exiting. If the current thread is calling TerminateThread or SuspendThread then it should not do this for a thread holding a critical section. $ !cs -s parameter2 - dump information about this critical section. $ ln parameter2 - to show symbols near the address of the critical section. This should help identify the leaked critical section. $ dps parameter4 - to dump the stack trace for this critical section initialization.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Thread ID.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Critical section debug information address.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;EXIT_THREAD_OWNS_LOCK</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Unloading DLL containing an active critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a DLL has a global variable containing a critical section and the DLL is unloaded but the critical section has not been deleted. To debug this stop use the following debugger commands: $ du parameter3 - to dump the name of the culprit DLL. $ .reload dllname or .reload dllname = parameter4 - to reload the symbols for that DLL. $ !cs -s parameter1 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the leaked critical section. $ dps parameter2 - to dump the stack trace for this critical section initialization.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;DLL name address.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;DLL base address.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_IN_UNLOADED_DLL</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Freeing heap block containing an active critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a heap allocation contains a critical section, the allocation is freed and the critical section has not been deleted. To debug this stop use the following debugger commands: $ !cs -s parameter1 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the leaked critical section. $ dps parameter2 - to dump the stack trace for this critical section initialization. $ parameter3 and parameter4 might help understand where this heap block was allocated (the size of the allocation is probably significant).</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Heap block address.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Heap block size.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_IN_FREED_HEAP</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Double initialized or corrupted critical section.</h3>
    <p></p><i>Probable cause</i><p>Usually this stop is generated if a critical section has been initialized more than one time. In this case parameter3 and parameter4 are the stack trace addresses for two of these initializations. Some other times it is possible to get this stop if the critical section or its debug information structure has been corrupted. In this second case it is possible that parameter3 and parameter4 are invalid and useless. To debug this stop: $ !cs -s -d parameter2 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This might help identify the critical section if this is a global variable. $ dps parameter3 and dps parameter4 - to identify the two code paths for initializing this critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of the debug information structure found in the active list.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;First initialization stack trace.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Second initialization stack trace.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_DOUBLE_INITIALIZE</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Free memory containing an active critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the memory containing a critical section was freed but the critical section has not been deleted using DeleteCriticalSection. To debug this stop use the following debugger commands: $ !cs -s -d parameter2 - dump information about this critical section. $ dps parameter3 - to identify the code path for initializing this critical section. In most cases the lock verifier detects immediately leaked critical sections contained in a heap allocation, a DLL range, a virtual memory allocation or a MapViewOfFile mapped memory range and issues different stops in these cases. So there are very few cases left for this verifier stop. The lock must be in a memory range freed by kernel-mode code or freed cross-process by APIs like VirtualFreeEx. Most typically this stop will be encountered if a previous stop (e.g. LOCK_IN_FREED_HEAP or LOCK_IN_UNLOADED_DLL) was continued by hitting `g' in the debugger console.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section debug information address.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_IN_FREED_MEMORY</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Corrupted critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the DebugInfo field of the critical section is pointing freed memory. Usually another valid DebugInfo structure is found in the active critical section list. Without corruption the two pointers should be identical. To debug this stop use the following debugger commands: $ !cs -s -d parameter3 - dump information about this critical section based on the current contents of the debug info structure found in the active list (this structure is rarely corrupted so usually this information is trustworthy). $ !cs -s parameter1 - dump information about this critical section based on the current contents of the critical section structure (the structure is corrupted already so sometimes this information is NOT trustworthy). $ dps parameter4 - to identify the code path for initializing this critical section. Dump the critical section at address parameter1 and look for the corruption pattern. With good symbols for ntdll.dl you can use the following commands: $ dt ntdll!_RTL_CRITICAL_SECTION LOCK_ADDRESS $ dt ntdll!_RTL_CRITICAL_SECTION_DEBUG DEBUG_ADDRESS</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Invalid debug information address of this critical section.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the debug information found in the active list.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Initialization stack trace.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_CORRUPTED</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Invalid critical section owner thread.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the owner thread ID is invalid in the current context. To debug this stop: $ !cs -s parameter1 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Owning thread.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected owning thread.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Critical section debug info address.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_INVALID_OWNER</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Invalid critical section recursion count.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the recursion count field of the critical section structure is invalid in the current context. To debug this stop: $ !cs -s parameter1 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Recursion count.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected recursion count.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Critical section debug info address.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_INVALID_RECURSION_COUNT</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Deleting critical section with invalid lock count.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a critical section is owned by a thread if it is deleted or if the critical section is uninitialized. To debug this stop: $ !cs -s parameter1 - dump information about this critical section. If the owning thread is 0 the critical section has not been initialized. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Lock count.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected lock count.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Owning thread.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_INVALID_LOCK_COUNT</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Critical section over-released or corrupted.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a critical section is released more times than the current thread acquired it. To debug this stop: $ !cs -s parameter1 - dump information about this critical section. $ !cs -s -d parameter4 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Lock count.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected lock count.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Critical section debug info address.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_OVER_RELEASED</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Critical section not initialized.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a critical section is used without being initialized or after it has been deleted. To debug this stop: $ ln parameter1 - to show symbols near the address of the critical section. This should help identify the critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section debug info address.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_NOT_INITIALIZED</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Critical section is already initialized.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if a critical section is reinitialized by the current thread. To debug this stop: $ !cs -s parameter1 or !cs -s -d parameter2 - dump information about this critical section. $ ln parameter1 - to show symbols near the address of the critical section. This might help identify the critical section if this is a global variable. $ dps parameter3 - to identify the code path for the first initialization of this critical section. $ kb - to display the current stack trace, that is reinitializing this critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section debug info address.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;First initialization stack trace. Use dps to dump it if non-NULL</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_ALREADY_INITIALIZED</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Freeing virtual memory containing an active critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the current thread is calling VirtualFree on a memory block that contains an active critical section. The application should call DeleteCriticalSection on this critical section before if frees this memory. $ kb - to display the current stack trace, that is calling VirtualFree. The probable culprit is the DLL that calls VirtualFree. $ !cs -s parameter1 - dump information about this critical section. $ dps parameter2 - to identify the code path for the initialization of this critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Memory block address.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Memory block size.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_IN_FREED_VMEM</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Unmapping memory region containing an active critical section.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the current thread is calling UnmapViewOfFile on a memory block that contains an active critical section. The application should call DeleteCriticalSection on this critical section before if unmaps this memory. $ kb - to display the current stack trace, that is calling UnmapViewOfFile . The probable culprit is the DLL that calls UnmapViewOfFile. $ !cs -s parameter1 - dump information about this critical section. $ dps parameter2 - to identify the code path for the initialization of this critical section.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Critical section initialization stack trace.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Memory block address.</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Memory block size.</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_IN_UNMAPPED_MEM</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Current thread does not own any critical sections.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the current thread is calling LeaveCriticalSection but, according to the internal verifier bookkeeping, it doesn't own any critical section. If parameter2 is zero, probably this is a bug in the current thread. It either tries to leave a critical section that it didn't enter, or maybe it is calling LeaveCriticalSection more times than it called EnterCriticalSection for the same critical section. If parameter2 is not zero (it is a negative integer number) the internal verifier data structures are probably corrupted.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Number of critical sections owned by current thread.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;THREAD_NOT_LOCK_OWNER</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>
    <h3>Using critical section that is private to another DLL.</h3>
    <p></p><i>Probable cause</i><p>This stop is generated if the current thread tries to use a private lock that lives inside another DLL. For example a.dll tries to enter a critical section defined inside ntdll.dll. Private locks cannot be used across DLLs.</p>
    <p></p><I>Information displayed by Application Verifier</I><ul>
      <li><b>Parameter 1</b>&nbsp;-&nbsp;Critical section address.</li>
      <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
      <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
      <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
    </ul>
    <p></p><i>Additional Information</i><ul>
      <li><b>Test Layer:</b>&nbsp;Locks</li>
      <li><b>Stop ID:</b>&nbsp;LOCK_PRIVATE</li>
      <li><b>Stop code:</b>&nbsp;200NAN</li>
      <li><b>Severity:</b>&nbsp;Error</li>
      <li><b>One-time error:</b>&nbsp;</li>
      <li><b>Error report:</b>&nbsp;Break</li>
      <li><b>Log to file:</b>&nbsp;yes</li>
      <li><b>Create backtrace:</b>&nbsp;yes</li>
    </ul>
    <p></p>



## SRWLock Stop Details

<h3>The SRW Lock is not initialized.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if a thread is trying to use the SRW lock (Param1) that is not initialized. $ kb - to get the current stack trace. This is where the SRW lock is being used. The SRW lock should be initialized using InitializeSRWLock before it can be used.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;NOT_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The SRW Lock is already initialized.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the SRW lock (Param1) is being re-initialized. If the SRW lock is being actively used by other threads, re-initializing the lock will result in unpredictable behavior by the application including hangs and crashes. The initialization stack trace may show an acquire if the SRW lock was statically initialized. $ kb - to get the current stack trace. This is where the SRW lock is being re-initialized. $ dps Param3 - to get the SRW lock initialization stack trace. This stack trace may show an acquire if the lock was statically initialized.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;ThreadId of the thread that initialized the SRW lock.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the initialization stack trace. Use dps &lt;address&gt; to see where the SRW lock was initialized. </li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;ALREADY_INITIALIZED</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Mismatched Acquire-Release on the SRW lock.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the SRW lock (Param1) is being released with a wrong release API. If the SRW lock was acquired for shared access and is being released using the exclusive release API or the SRW lock was acquired for exclusive access and is being release using the shared release API. This can result in unpredictable behavior by the application including hangs and crashes. $ kb - to get the current stack trace. This is where the SRW lock is being released using the wrong API. $ dps Param3 - to get the SRW lock acquire stack trace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;ThreadId of the thread that acquired the SRW lock.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired. </li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;MISMATCHED_ACQUIRE_RELEASE</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The SRW lock is being acquired recursively by the same thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the SRW lock (Param1) is being acquired recursively by the same thread. This will result in a deadlock and the thread would block indefinitely. Recursive acquisition of an SRW lock in exclusive mode will cause a deadlock. Recursive acquisition of an SRW lock in shared mode will cause a deadlock when there is a thread waiting for exclusive access. Consider the example below: - Thread A acquires the SRW lock in shared mode - Thread B tries to acruire the SRW lock in exclusive mode and waits - Thread A tries to acquire the SRW lock in shared mode recursively. This will be successful as long as there is no exclusive waiter (in this case B). Since SRW locks do not have writer starvation, thread A waits behind thread B. Now, Thread B is waiting for Thread A which is inturn waiting for Thread B causing a circular wait and hence a deadlock. $ kb - to get the current stack trace. This is where the SRW lock is being acquired recursively. $ dps Param2 - to get the stack trace for the first acquire.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of the first acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;RECURSIVE_ACQUIRE</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The thread that is exiting or being terminated owns an SRW lock.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the thread (Param2) that owns the SRW lock (Param1) is exiting or being terminated. This will result in an orphaned SRW lock and the threads trying to acquire this lock would block indefinitely. $ kb - to get the current stack trace. This is where the thread is exiting or is being terminated. $ dps Param3 - to get the SRW lock acquire stack trace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;ThreadId of the thread that is exiting or being terminated.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of the acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired. </li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;EXIT_THREAD_OWNS_LOCK</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The SRW lock being released was not acquired by this thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the SRW lock (Param1) is being released by the thread (Param2) that didn't acquire the lock. This represents bad programming practice that is hard to get right and can lead to unpredictable behavior by the application. $ kb - to get the current stack trace. This is where the thread is releasing the SRW lock that it didn't acquire. $ dps Param4 - to get the SRW lock acquire stack trace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Current ThreadId.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;ThreadId of the thread that acquired the SRW lock.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of the acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired. </li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_OWNER</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The memory being freed contains an active SRW lock.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the memory address (Param1) being freed contains an active SRW lock that is still in use. This can result in unpredictable behavior by the application including crashes and hangs. $ kb - to get the current stack trace. This is where the memory is being freed that contains an active SRW lock. $ dps Param4 - to get the SRW lock acquire stack trace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of the memory being freed.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;ThreadId of the thread that acquired the SRW lock.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of the acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired. </li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;IN_FREED_MEMORY</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The DLL being unloaded contains an active SRW lock.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the DLL being unloaded (Param2) contains an active SRW lock (Param1) that is still in use. This can result in unpredictable behavior by the application including crashes and hangs. $ kb - to get the current stack trace. This is where the DLL is being unloaded that contains an active SRW lock. $ du Param2 - to find the name of the DLL that is being unloaded. $ dps Param4 - to get the SRW lock acquire stack trace.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;SRW Lock</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of the name of the DLL being unloaded. Use du &lt;address&gt; to see the name.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;ThreadId of the thread that acquired the SRW lock.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Address of the acquire stack trace. Use dps &lt;address&gt; to see where the SRW lock was acquired. </li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;SRWLock</li>
  <li><b>Stop ID:</b>&nbsp;IN_UNLOADED_DLL</li>
  <li><b>Stop code:</b>&nbsp;250NAN</li>
  <li><b>Severity:</b>&nbsp;Warning</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;None</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>


## Memory Stop Details

<h3>Freeing virtual memory block with invalid size or start address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree or a DLL unload with an invalid start address or size of the memory allocation. In the case of DLL unload this probably means a memory corruption inside the loaded DLL list. To debug this stop look at the current stack trace and the memory address and size that is about to be freed and try to determine why they are invalid.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Allocation base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory region size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FREEMEM</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect virtual alloc call.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualAlloc call with an invalid start address or size of the memory allocation. To debug this stop look at the current stack trace (kb) and the memory address and size that is about to be allocated and try to determine why they are invalid.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Pointer to allocation base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Pointer to memory region size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_ALLOCMEM</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect map view call.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a MapViewOfFile call with an invalid base address or size of the mapping. To debug this stop look at the current stack trace (kb) and the memory address and size that is about to be mapped and try to determine why they are invalid.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Pointer to mapping base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Pointer to view size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_MAPVIEW</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Probing invalid address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an IsBadXXXPtr call with an invalid address (e.g. a kernel-mode address, instead of a normal user-mode address) for the memory buffer to be probed. To debug this stop look at the current stack trace (kb) and try to determine why the caller of the IsBadXXXPtr function ended up with an invalid address. Many times, the address is plain bogus, e.g. an uninitialized pointer. MSDN library lists a few reasons why applications should not use the IsBadXXXPtr APIs: In a preemptive multitasking environment, it is possible for some other thread to change the process's access to the memory being tested. Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. Threads in a process are expected to cooperate in such a way that one will not free memory that the other needs. Use of this function does not negate the need to do this. If this is not done, the application may fail in an unpredictable manner. Because of all these reasons, we recommend to never use these APIs.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Start address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory block size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Invalid address.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_INVALID_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Probing free memory.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an IsBadXXXPtr call for a memory allocation that is free. This is very bad because it is possible that, in some other cases, this memory was already reused for some other allocation. Since the current code path (kb) doesn't own that memory, it could end up corrupting someone else's memory, with disastrous effects. To debug this stop look at the current stack trace (kb) and try to determine why the caller of the IsBadXXXPtr function ended up probing free memory. The address could be plain bogus (e.g. uninitialized pointer) or maybe already freed memory. If the memory was already freed by one of the VirtualFree or UnmapViewOfFile APIs, `!avrf -vs -a parameter3' will search for a log of stack traces of the code paths that allocated/freed that address and display these stack traces if they are available. This might show the stack trace that freed up this memory. More often, the memory is an already freed heap allocation. To check for that possibility, `!avrf -hp -a parameter3' will search for a log of stack traces of the code paths that allocated/freed that address from/to the heap and display these stack traces if they are available. MSDN library lists a few reasons why applications should not use the IsBadXXXPtr APIs: In a preemptive multitasking environment, it is possible for some other thread to change the process's access to the memory being tested. Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. Threads in a process are expected to cooperate in such a way that one will not free memory that the other needs. Use of this function does not negate the need to do this. If this is not done, the application may fail in an unpredictable manner. Because of all these reasons, we recommend to never use these APIs.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Start address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory block size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of free memory page.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_FREE_MEM</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Probing a guard page.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an IsBadXXXPtr call for a memory allocation that contains at least one GUARD_PAGE. This is very bad because it is very possible that this GUARD_PAGE is the end of the current stack of a thread. As documented in the MSDN library: Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. To debug this stop look at the current stack trace (kb) and try to determine why the caller of the IsBadXXXPtr function ended up probing a GUARD_PAGE. MSDN library lists a few reasons why applications should not use the IsBadXXXPtr APIs: In a preemptive multitasking environment, it is possible for some other thread to change the process's access to the memory being tested. Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. Threads in a process are expected to cooperate in such a way that one will not free memory that the other needs. Use of this function does not negate the need to do this. If this is not done, the application may fail in an unpredictable manner. Because of all these reasons, we recommend to never use these APIs.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Start address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory block size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Address of guard page.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_GUARD_PAGE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Probing NULL address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an IsBadXXXPtr call with a NULL address. To debug this stop look at the current stack trace (kb) and try to determine why the caller of the IsBadXXXPtr function ended up with the NULL address. This is typically the sign of someone not checking the return value of one of the memory allocation functions. For example the code below is incorrect: int main (void) { PVOID p; p = malloc (1024); Use (p); return 0; } void Use (PVOID p) { if (IsBadReadPtr (p)) { return; } // // p is safe to be used here. // } This code should be re-written as this: int main (void) { PVOID p; p = malloc (1024); if (NULL == p)) { return -1; } Use (p); return 0; } void Use (PVOID p) { // // p is safe to be used here. // } MSDN library lists a few reasons why applications should not use the IsBadXXXPtr APIs: In a preemptive multitasking environment, it is possible for some other thread to change the process's access to the memory being tested. Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. Threads in a process are expected to cooperate in such a way that one will not free memory that the other needs. Use of this function does not negate the need to do this. If this is not done, the application may fail in an unpredictable manner. Because of all these reasons, we recommend to never use these APIs.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_NULL</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Probing memory block with invalid start address or size.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an IsBadXXXPtr call with an invalid start address (e.g. a kernel-mode address, instead of a normal user-mode address) or invalid size for the memory buffer to be probed. To debug this stop look at the current stack trace (kb) and try to determine why the caller of the IsBadXXXPtr function ended up with an invalid address or size. Many times, the address or size are plain bogus, e.g. an uninitialized variables. MSDN library lists a few reasons why applications should not use the IsBadXXXPtr APIs: In a preemptive multitasking environment, it is possible for some other thread to change the process's access to the memory being tested. Dereferencing potentially invalid pointers can disable stack expansion in other threads. A thread exhausting its stack, when stack expansion has been disabled, results in the immediate termination of the parent process, with no pop-up error window or diagnostic information. Threads in a process are expected to cooperate in such a way that one will not free memory that the other needs. Use of this function does not negate the need to do this. If this is not done, the application may fail in an unpredictable manner. Because of all these reasons, we recommend to never use these APIs.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Start address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory block size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_INVALID_START_OR_SIZE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unloading DLL with invalid size or start address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a DLL unload with an invalid start address or size of the DLL memory range. This probably means a memory corruption inside the internal ntdll.dll loaded DLL list.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;DLL memory base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;DLL memory range size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;DLL name address. Use du to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_DLL_RANGE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Freeing memory block inside current thread's stack address range.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree for a block of memory that is actually part of the current thread's stack (!). To debug this stop look at the current stack trace (kb) and try to understand why the function that called VirtualFree thought that the memory block was dynamically allocated or mapped but that was actually memory allocated from the stack.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Allocation base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory region size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Stack low limit address.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Stack high limit address.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;FREE_THREAD_STACK_MEMORY</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect FreeType parameter for VirtualFree operation.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree with an incorrect value for the FreeType parameter. The only two acceptable values for this parameter are MEM_DECOMMIT and MEM_RELEASE. If VirtualFree is called with any other value except these two, VirtualFree will fail to free the memory. To debug this stop look at the current stack trace (kb): the caller of VirtualFree is probably the culprit.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Incorrect value used by the application.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected correct value 1.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Expected correct value 2.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FREE_TYPE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Trying to free virtual memory block that is already free.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree for an address that is already free. To debug this stop look at the current stack trace (kb) and try to determine why the memory is already free but the application is trying to free it again. `!avrf -vs -a parameter1' will search for a log of stack traces of the code paths that allocated/freed that address and display these stack traces if they are available. This might show the stack trace that freed up this memory.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Memory block address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;MEM_ALREADY_FREE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect Size parameter for VirtualFree (MEM_RELEASE) operation.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree (MEM_RELEASE) with a non-zero value for the dwSize parameter. When using MEM_RELEASE , the only acceptable value for this parameter is 0. If VirtualFree is called with any other value except 0, VirtualFree will fail to free the memory. To debug this stop look at the current stack trace (kb): the caller of VirtualFree is probably the culprit.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Incorrect size used by the application.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected correct size (0).</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FREE_SIZE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception raised in DLL entry point routine.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if a DLL's entry point (DllMain) function is raising an exception. One example why this is bad is: if DllMain(DLL_PROCESS_ATTACH) is raising an exception, the Windows DLL loader will: - Catch and hide the exception; - Unload the DLL without calling its DllMain(DLL_PROCESS_DETACH). So in many cases the DLL allocated some resources already, then it raised the exception, and it will not have a chance to release these resources on DllMain (DLL_PROCESS_DETACH). To debug this stop: $ du parameter1 - to display the DLL name; $ .exr parameter2 - to display the exception information; $ .cxr parameter3 followed by kb - to display the exception context information and the stack trace for the time when the exception was raised; $ parameter4 is the address of an internal verifier structure and doesn't have any significance for most of the verifier users.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;DLL name (use du to dump it).</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Verifier dll descriptor</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;DLL_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception raised in thread function.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if a thread function is raising an exception. This is bad because the whole process will be killed. To debug this stop: $ parameter1 might be significant for the type of exception. E.g. an exception code C0000005 means Access Violation; $ .exr parameter2 - to display the exception information; $ .cxr parameter3 followed by kb - to display the exception context information;</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exception code.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;THREAD_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception raised while probing memory.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if we get an exception during an IsBadXXXPtr call. This means that the memory buffer we are probing doesn't actually have the protection assumed by the caller, or that the memory was freed already, etc. See the discussion above about other stop code (PROBE_INVALID_ADDRESS, PROBE_FREE_MEM, PROBE_GUARD_PAGE, PROBE_NULL, PROBE_INVALID_START_OR_SIZE) for more examples of why using the IsBadXXXPtr APIs is not recommended. To debug this stop: $ parameter1 will typically be C0000005 and that means Access Violation; $ .exr parameter2 - to display the exception information; $ .cxr parameter3 followed by kb - to display the exception context information and stack trace at the time when the exception was raised;</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exception code.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;PROBE_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Trying to reset NULL address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a VirtualFree (MEM_RESET) call with a NULL first parameter. MEM_RESET should be used only for already allocated memory, so NULL is not a valid first parameter in this case.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_MEM_RESET</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Freeing heap memory block inside current thread's stack address range.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects a HeapFree, for a block of memory that is actually part of the current thread's stack (!). To debug this stop look at the current stack trace (kb) and try to understand why the function that called HeapFree thought that the memory block was dynamically allocated or mapped but that was actually memory allocated from the stack.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Allocation base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory region size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Stack low limit address.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Stack high limit address.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;FREE_THREAD_STACK_MEMORY_AS_HEAP</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unmapping memory region inside current thread's stack address range.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the app verifier detects an UnmapViewOfFile, for a block of memory that is actually part of the current thread's stack (!). To debug this stop look at the current stack trace (kb) and try to understand why the function that called UnmapViewOfFile thought that the memory block was dynamically allocated or mapped but that was actually memory allocated from the stack.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Allocation base address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Memory region size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Stack low limit address.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Stack high limit address.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;FREE_THREAD_STACK_MEMORY_AS_MAP</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Incorrect RTL_RESOURCE address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is trying to use NULL or some other incorrect address (e.g. a kernel-mode address) as the address of a valid object. RtlInitializeResource (NULL) is an incorrect API call that will trigger this kind of verifier stop. param1 is the incorrect address used and the culprit is on the stack trace (display it with kb).</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_RESOURCE_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Invalid critical section address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is trying to use NULL or some other incorrect address (e.g. a kernel-mode address) as the address of a valid object. EnterCriticalSection(NULL) is an incorrect API call that will trigger this kind of verifier stop. param1 is the incorrect address used and the culprit is on the stack trace (display it with kb).</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_CRITSECT_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Attempt to execute code in non-executable memory.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is trying to run code from an address that is non-executable or free. To debug this stop: $ u parameter2 - to unassemble the culprit code $ .exr parameter3 - to display the exception information; $ .cxr parameter4 followed by kb - to display the exception context information and the stack trace for the time when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address being accessed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code performing invalid access.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;THREAD_UNEXPECTED_EXCEPTION_CODE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception raised while initializing output buffer.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if we get an exception while initializing a buffer specified as output parameter for a Win32 or CRT API. This typically means that the specified output buffer size is incorrect. To debug this stop: $ .exr parameter3 - to display the exception information; $ .cxr parameter4 followed by kb - to display the exception context information and stack trace at the time when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Buffer start address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Buffer size.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;OUTBUFF_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unexpected exception when trying to find heap block size.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if we get an exception while calling HeapSize for a heap block that is being freed. This typically means that the specified heap block address is incorrect or the heap is corrupted. To debug this stop: $ .exr parameter3 - to display the exception record; $ .cxr parameter4 followed by kb - to display the exception context information and stack trace at the time when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of the heap block being freed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Heap handle.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;SIZE_HEAP_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Freeing memory block with invalid start address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the program calls VirtualFree (MEM_RELEASE) with an lpAddress parameter that is not the base address returned by the VirtualAlloc or VirtualAllocEx function when the region of pages was reserved; To debug this stop: $ kb - to display the current stack trace, that is calling VirtualFree. The probable culprit is the DLL that calls VirtualFree.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of memory block being freed.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected correct memory block address.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_FREEMEM_START_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unmapping memory block with invalid start address.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the program calls UnmapViewOfFile with an lpBaseAddress parameter that is not identical to the value returned by a previous call to the MapViewOfFile or MapViewOfFileEx function. To debug this stop: $ kb - to display the current stack trace, that is calling UnmapViewOfFile. The probable culprit is the DLL that calls UnmapViewOfFile.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address of memory block being unmapped.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected correct memory block address.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_UNMAPVIEW_START_ADDRESS</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>unexpected exception raised in threadpool callback function.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if a callback function in the threadpool thread is raising an exception. To debug this stop: $ parameter1 might be significant for the type of exception. E.g. an exception code C0000005 means Access Violation. $ .exr parameter2 - to display the exception information. $ .cxr parameter3 followed by kb - to display the exception context information.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Exception code</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Exception record. Use .exr to display it</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Context record. Use .cxr to display it</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;THREADPOOL_UNEXPECTED_EXCEPTION</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>code in non-executable memory</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is trying to run code from an address that is non-executable or free. To debug this stop: $ u parameter2 - to unassemble the culprit code $ .exr parameter3 - to display the exception information $ .cxr parameter4 followed by kb - to display the exception context information and the stack trace for the time when the exception was raised.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Address being accessed</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Code performing invalid access</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Exception record. Use .exr to display it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Context record. Use .cxr to display it.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;THREADPOOL_UNEXPECTED_EXCEPTION_CODE</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Creating executable heap.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is creating an executable heap. This can be a security risk.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;EXECUTABLE_HEAP</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Allocating executable memory.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the application is allocating executable memory. This can be a security risk.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Page protection specified by caller.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Memory</li>
  <li><b>Stop ID:</b>&nbsp;EXECUTABLE_MEMORY</li>
  <li><b>Stop code:</b>&nbsp;600NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>

## TLS Stop Details

<h3>Unloading DLL that allocated TLS index that was not freed.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if a DLL that allocated a TLS index is being unloaded before freeing that TLS index. To debug this stop: $ du parameter3 - display the name of the culprit DLL; $ .reload xxx.dll=parameter4 - reload symbols for the culprit DLL (if needed). xxx.dll is the name of the DLL displayed in the above step; $ u parameter2 - disassemble the code that allocated the TLS. This should point to the function that allocated the TLS but forgot to free it before the DLL was unloaded.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;TLS index</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Address of the code that allocated this TLS index.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;DLL name address. Use du to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;DLL base address.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;TLS</li>
  <li><b>Stop ID:</b>&nbsp;TLS_LEAK</li>
  <li><b>Stop code:</b>&nbsp;350NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Corrupted verifier TLS structure.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the internal verifier structures used to store the state of TLS slots for thread are corrupted. Very likely this is due to some random corruption in the process.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;TEB address.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Expected TEB address.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Thread ID.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Expected thread ID.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;TLS</li>
  <li><b>Stop ID:</b>&nbsp;CORRUPTED_TLS</li>
  <li><b>Stop code:</b>&nbsp;350NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Using an invalid TLS index.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if an invalid TLS index is used. In most cases, it's because code is still using this index when TlsFree is called. Here is an example for the threadpool thread. T1: Dll loads and TlsAlloc T1: Queue callback T1: Skipped waited/cancelled callback T1: TlsFree T2: Callback runs and calls TlsSetValue T1: Dll unloads</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;TLS index</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;TLS</li>
  <li><b>Stop ID:</b>&nbsp;INVALID_TLS_INDEX</li>
  <li><b>Stop code:</b>&nbsp;350NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>


## Threadpool Stop Details

<h3>The priority of this threadpool thread has been changed.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the thread priority is changed when it's returned to threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; threadpool thread (%x) having executed Callback (%p) has an altered thread priority (%i -&gt; %i) </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Current Priority.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;INCONSISTENT_PRIORITY</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The affinity of this threadpool thread has been changed.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the thread affinity is changed when it's returned to threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;threadpool thread (%x) having executed Callback (%p) has an altered thread affinity mask (%p -&gt; %p) </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Current affinity.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;INCONSISTENT_AFFINITY_MASK</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unprocessed msg in the msg pool of current thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if any message left as unprocessed when this threadpool thread is returned to the pool. It's dangerous since it will be processed in a totally different context. Please use Please use !avrf -tp &lt;Param4&gt; to see the messages posted to this thread.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp;threadpool thread (%x) having executed Callback (%p) has outstanding window message (%x: %x) </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Threadpool thread id. Please use !avrf -tp &lt;threadid&gt; to see the messages posted to this thread.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;ORPHANED_THREAD_MESSAGE</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Unclosed window belonged to the current thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if any window is kept alive when this threadpool thread is returned to the pool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Format:</b>&nbsp;-&nbsp; threadpool thread (%x) having executed Callback (%p) has valid hwnd (%x: %s) which could receive messages </li>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Threadpool thread id.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;ORPHANED_THREAD_WINDOW</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>ExitThread() on a threadpool thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if ExitThread is called on a threadpool thread.It's forbidden since it will make system unstable. It will cause resource leak, freeze or AV.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;ILLEGAL_THREAD_EXIT</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Thread is in impersonation state when it's returned to a threadpool thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if call back function change the thread token to impersonate another user and forgot to reset it before returning it back to the threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;THREAD_IN_IMPERSONATION</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>A function which requires persistent thread is called.</h3>
<p></p><i>Probable cause</i><p>Some Microsoft Windows APIs need to be called inside a dedicated or persistent thread. In the threadpool you should generally avoid using thread local storage and queuing asynchronous calls that require a persistent thread, such as the RegNotifyChangeKeyValue function. However, such functions can be queued to a persistent worker thread using QueueUserWorkItem with the WT_EXECUTEINPERSISTENTTHREAD option. A kb in debugger will reveal the caller.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;PERSISTED_THREAD_NEEDED</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>Thread is in dirty transaction state.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if call back function forgot to close or reset the current transaction handle.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Transaction Handle.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;DIRTY_TRANSACTION_CONTEXT</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>This threadpool state has unbalanced CoInit and CoUnInit calls.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if call back function calls CoInit and CoUnInit unbalanced.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Balanced Call counts.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;DIRTY_COM_STATE</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The parameters for the timer object are inconsistent. Period should be 0 when WT_EXECUTEONLYONCE is specified when creating the timer</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the period to signal the timer is not zero when the timer is set to signal only once with the WT_EXECUTEONLYONCE flag</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Period specified.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Flags specified.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;INCONSISTENT_TIMER_PARAMS</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The loader lock has been held by the threadpool thread within the callback.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the loader lock is held within the callback and is not released when the thread is returned to the threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;LOADER_LOCK_HELD</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The preferred language is set by the threadpool thread within the callback.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the preferred language is set within the callback and is not cleared when the thread is returned to the threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;PREFERRED_LANGUAGES_SET</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>The background priority is set by the threadpool thread within the callback.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if the background priority is set within the callback and is not disabled when the thread is returned to the threadpool.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Callback function.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Context.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Threadpool Object allocation stack trace, use dps to dump it.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;BACKGROUND_PRIORITY_SET</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>
<h3>TerminateThread() on a threadpool thread.</h3>
<p></p><i>Probable cause</i><p>This stop is generated if TerminateThread is called on a threadpool thread. It's forbidden since it will make system unstable. It will cause resource leak, freeze or AV.</p>
<p></p><I>Information displayed by Application Verifier</I><ul>
  <li><b>Parameter 1</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 2</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 3</b>&nbsp;-&nbsp;Not Used.</li>
  <li><b>Parameter 4</b>&nbsp;-&nbsp;Not Used.</li>
</ul>
<p></p><i>Additional Information</i><ul>
  <li><b>Test Layer:</b>&nbsp;Threadpool</li>
  <li><b>Stop ID:</b>&nbsp;ILLEGAL_THREAD_TERMINATION</li>
  <li><b>Stop code:</b>&nbsp;700NAN</li>
  <li><b>Severity:</b>&nbsp;Error</li>
  <li><b>One-time error:</b>&nbsp;</li>
  <li><b>Error report:</b>&nbsp;Break</li>
  <li><b>Log to file:</b>&nbsp;yes</li>
  <li><b>Create backtrace:</b>&nbsp;yes</li>
</ul>
<p></p>

 ## See Also

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)
  
[Application Verifier - Frequently Asked Questions](application-verifier-faqs.md)


 





