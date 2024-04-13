---
title: Application Verifier - Frequently Asked Questions (FAQs)
description: Application Verifier- Frequently Asked Questions (FAQs)
keywords:
- verifying drivers (Application Verifier)
- driver verification (Application Verifier)
- Application Verifier
- AppVerif.exe
- user-mode application testing
ms.date: 01/12/2022
---

# Application Verifier - Frequently Asked Questions (FAQs)
 
## General Questions 
 
Following is a list of questions received around the general usage of Application Verifier. 

*What is Application Verifier?*

Application Verifier is a runtime verification tool used to find bugs in Microsoft Windows-applications. Since it is a runtime tool the application code needs to be exercised in order to be verified. Good test coverage is therefore essential. 

The typical usage scenario of Application Verifier is to enable it for the applications of interest (see questions below for how to do that) and then run all the tests you have written for your application. You will get a notification for any bug found in the form of a debugger break or a verifier log entry. 

*How do I uninstall Application Verifier?*

To uninstall the Application Verifier, access the control panel by clicking Start, select Add or Remove Programs, then Remove a program, click Application Verifier, and then click Remove. 

*How do I start Application Verifier?*

After installing Application Verifier you can either start it by accessing it in your list of programs OR by typing Appverif.exe on a command line. To do this, go to a command prompt or the Run box of the Startup menu. Type appverif.exe and then press Enter. This will start Application Verifier.

The Appverifer.exe binary is installed in the system directory and is used to make the tool settings. 

*Where are the logs stored?*

The logs are stored in %USERPROFILE%\AppVerifierLogs

*What should I do if I have problems while using the Application Verifier?*

Make sure you are running the latest release. Consider trying the same app on a different PC or even version of Windows.

*Does Application Verifier verify managed code?*

AppVerifier cares about the interfaces between the operating system and the application. As a result, unless your managed code is performing interop against native APIs that have to do with Heaps, Handles, Critical Section, etc. your test cases are not going to give you any interaction with the interfaces that are verified. 

We recommend leveraging the Managed Debugging Assistants for verifying your managed code. Read more about them at [Debugging Managed Code Using the Windows Debugger](../debugger/debugging-managed-code.md).

 
## Debugger Questions 
 
Following are the list of questions received regarding the debugger. 

*Why did I receive an error telling me I need a debugger?*

The Basics verification layer within Application Verifier require that you run your application under a debugger. If you do not have a debugger associated to the application prior to selecting the test, you will receive a dialog reminding you that you will need to run your application under a debugger in order to obtain the logged information. 

*How do I run my application under a debugger?*

See the Debugger install and setup topics - [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md)

*How do I test stack expansion without any other instrumentation?*

In general, stack expansion should be really tested in isolation from other verification layers, including heap. The reason is the following: each verification layers "thunks" an API or an exported point with some routine. 

For example, a call to CreateFileA, will be a call to appvocre!NS_SecurityChecks::CreateFileA, that might call appvcore!NS_FillePaths::CreateFileA that might call kernel32!CreateFileA, that might call verifier!AVrfpNtCreateFile, that will call ntdll!NtCreateFile. You can see that the instrumentation has added 3 more "stacked" function calls, each one of them may and will consume more stack. 

In the case below, the LH-verifier.dll is "thunking" every DllMain, and the "instrumented" heap code path will add more stack usage. Since the injected thread from the debugger does not use the IMAGE_NT_HEADERS defaults, the initially committed stack will not be enough to complete the APC state of a thread (a thread in the APC state executed the initialization code). 

If you want to use Stack-Ckecs, probably the only other verification layer you should use if FirstChanceAccessViolation. 

*When using !avrf extension I get 'Application verifier is not enabled for this process...'*

The complete error received: `Application verifier is not enabled for this process. Use appverif.exe tool to enable it.`

You probably have just the shim verification layers enabled and/or the heap in "pure" mode enabled. These are some of the possible causes. 
 
## Testing Scenario Questions 
 
Following is a list of questions received around different testing scenarios. 

*How can I enable Application Verifier on my service but not others?*

Make a copy of svchost.exe in the System32 directory and call the copy “Mysvchost.exe”.

Using regedit, open HKLM\System\CurrentControlSet\Services\MyService.

Edit the value “ImagePath”, which will be something like “%SystemRoot%\system32\svchost.exe -k myservice” and change svchost.exe to “Mysvchost.exe”.

Add “Mysvchost.exe” to the AppVerifier list and check the tests desired.

Reboot.

*How do I run Application Verifier on a 64-bit application that is launched from a 32-bit application running under WOW64?*

Simple version: The golden rule for enabling verifier settings on a given application is to match the bit-ness of the tool and the target process. That is: use the 32-bit appverif.exe for a 32-bit application (both running under WoW64) and use the 64-bit AppVerif.exe for the native 64-bit native target. 

Long Version: Application Verifier settings are the proper union of "core" settings and "shim" settings. 

Core settings - Core settings are stored under Image File Execution Options.

The "Debugger" value is read from the launching application. So, if you want to have 32-bit devenv.exe launching 64-bit my.exe and have it running under debugger, you must use the 32-bit registry key under WoW6432Node. The other values, for a 32-bit process, are read from both places, both the native IFEO and the WoW6432Node.

The reasoning is the following: a 32-bit process running under WoW is a 64-bit process running the Wow64 emulation loop. So, each 32-bit process is first a 64-bit process, and then a 32-bit process. The 64-bit IFEO will enable verifier on the Wow64cpu.dll code, while the 32-bit IFEO will enable verifier on the 32-bit code.

From the end-user point of view, verifier.dll is loaded twice (once in the 64-bit world, once in the 32-bit world). Since most of the people do not care about verifying wow64cpu.dll, the most accepted behavior for 32-bit processes is to only verify the 32-bit part. That is why the golden rule of "always match the bit-ness" applies. 

*How do I debug my service that runs in a non-interactive window station*

To debug a service that runs in a non-interactive window station, do the following (only applies if you’re using ntsd/windbg): 

Add a key to the registry under HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options. The name of this key should be the name of the process (service.exe). 

Create a REG_SZ value called Debugger and set this value to the path where your debugger resides. It must contain the full path, not just the name of the debugger. The command should include the –server option and a specific port or port range that the debugger should listen on. An example is c:\debuggers\ntsd.exe –server tcp:port=5500:5600 –g –G. 

Connect to the debugger server by running the debugger with a –remote option. An example is: windbg.exe –remote tcp:=localhost,port=55xx where ‘xx’ is some number from 00 to 99 if you used a range on the server. 

Does AppVerifier do leak detection?
Under Windows 7 and greater, there is a Leaks check option that will detect when a process leaks memory. Under earlier operating systems, AppVerifier does not test application for leak detection but looks for other memory issues.

*Which tests are recommended for security concerns?*

- Heaps 
- Handles 
- Locks 
- Stacks (only for services and important processes that can take machine down) 

Keep in mind that ObsoleteAPICalls will just spit out a warning for every call it sees to an API that is listed as obsolete or deprecated in MSDN. You should decide on a case by case basis if it is important for your application to switch to the new APIs. Some of the APIs are dangerous, and some have merely been superseded by a newer API with more options. Take a look at the "Dangerous APIs" section of Writing Secure Code, 2nd addition for more. 

For applications that need to be highly reliable, like services and server programs, you should also enable the Stacks check. This checks to see if the stack commit size is adequate, by disabling stack growth. If the application quits immediately with a stack overflow, that means the application needs to be recompiled with a larger stack commit size. If you're a tester, and encounter a problem with an application while using the Stacks check, file a bug, assign it to your developer, and keep on testing.

## Test Specific Questions 
 
Following is a list of questions around testing. Click on the question to see the response: 

*Are critical section leaks important?*

Whenever you leak a critical section you leak the following: an event handle, a small amount of kernel pool and a small heap allocation. These will get cleaned up if the process exits. 

If your process is supposed to stay alive a long time, then these leaks can bite you. Since the fixes are very easy in 99% of the cases (developer just forgot to call RtlDeleteCriticalSection) you should address them. 

*Can we deal programmatically with stack overflows?*

Establishing an exception handler in the initial thread function is not guaranteed to catch the potential stack overflows that might be raised. This is because the code that dispatches exceptions needs also a little bit of stack to execute on top of the current activation record. Since we just failed the stack extension it is very likely that we will step over the end of the committed stack and raise a second exception while trying to dispatch the first one. A double fault exception will terminate the process unconditionally. 

The LoaderLock test is giving an error about calling DestroyWindow. Why can’t I call DestroyWindow in DllMain?
You do not control which thread is going to detach. If it is not the same thread that created the window, you cannot destroy the window. So you leak the window and the next time the window receives a message, you crash because the Wndproc has been unloaded. 

You need to destroy the window before you get the process-detach. The danger is not that user32 will be unloaded. The danger is that you are being unloaded. So the next message that the window receives will crash the process because user32 will deliver the message to your Wndproc which does not exist any more. 

Microsoft Windows operating system has thread affinity. Process-detach does not. The loader lock is not really the big problem; the problem is Dllmain. Process-detach is the last time your DLL gets to run code. You must get rid of everything before you return. But since Windows has thread affinity, you cannot clean up the window if you are on the wrong thread. 

The loader lock enters into the picture if somebody has a global hook installed (e.g., spy++ is running). In this case, you enter a potential deadlock scenario. Again, the solution is to destroy the window before you get process-detach. 

*Is it expensive to increase initial stack commits to avoid overflows?*

When you commit stack you are just reserving page file space. There is no performance impact. No physical memory is actually used. The only additional cost happens if you actually touch the stack space that you committed. But this will happen anyway even if you do not commit the stack upfront. 

Let us see what would be the cost to make all services running in svchost.exe bulletproof. On a test machine, I get 9 svchost.exe processes having a total of 139 threads. If we set the default stack for each thread at 32K we will need roughly 32K x 200 ~ 6.4 Mb of page file space to commit all stacks upfront. 

This is a pretty small price to pay for reliability. 

*What about reserved stack size?*

There are interesting items, such as exception dispatching on IA64/AMD64 that requires "unexpected" extra stack. There might be some processing happening on RPC worker threads whose stack requirements are past reasonable attempts to measure them. 

First of all, you should get an idea of all the thread pools living in the process. The NT-Thread-Pool, with the alertable-wait-threads is sometimes special, because, for example, if you use a database component from SQL, it will use alertable sleeps over a thread that is a target of user-APC. This can cause problems with nested calls.

Once you know all the thread pools, get an idea of how to control their stack requirements. For Example, RPC reads a registry key for the stack commit. The WDM pump threads get that from the image. For Other Thread Pools, the mileage may vary. 

When you all threads are clear you can take some action. Not having a huge reserved space helps address space fragmentation only if threads comes and goes very often. If you have a stable thread pool that is in your control, then you might have an advantage in reducing the reserved space as well. It will really help in saving address space for the heaps and address space for users. 

*Are there recommendations on how to pick the right size for LINKER_STACKCOMMITSIZE=?*

The value should be divisible by the page size (4k/8k depending on the CPU). Here are some guidelines to determine the size you need would do: 

1. Convert any recursive functions with potential unbound depth (or at least user inducible high depth) to iterative. 

2. Reduce alloca usage. Use heap or safealloca. 

3. Run Prefast with reduced stack size checking (say 8k). Fix those functions flagged as using too much stack. 

4. Set the stack commit to 16k. 

5. Run under a debugger bunch of tests with Application Verifier's "Stacks" check on. 

6. When you see stack overflow determine the worst offenders and fix them. (See step 5.) 

7. When you cannot reduce the stack usage any more bump by 8k. If you are > 64k there is something wrong, decrease back to 64k and see step 6. Otherwise go to step 5. 

*What are the memory requirements for the heap test?*

For full heap tests, you'll need 256MB of RAM and at least a 1GB page file. For normal heap tests, you'll need at least 128MB of RAM. There are no specific processor or disk requirements. 

*Why am I receiving an ALL_ACCESS stop?*

Any application that uses _ALL_ACCESS renders the object it is accessing unauditable because the audit log will not reflect what you have actually done with the object—only what you asked to do with the object. 

This condition creates a camouflage for a more devious attack. An administrator scanning for an attack activity in progress will see nothing wrong with the person requesting ALL_ACCESS on key X, because a particular application always does that. The administrator will think "the person is probably just running Word". The administrator cannot tell that a hacker has penetrated my account and is now probing the system to determine what access I have, which he can exploit for his nefarious ends. The possibilities are endless. 

The ACL issue with ALL_ACCESS is that you must always be granted it. If we wanted to someday deny you DELETE access to a certain key, we would not be able to. Even though you were not actually deleting the key, we would be breaking your application because you would request delete access. 

*Why don’t I get any logs from the heap and lock tests?*

Those tests are verification layers built in the operative system (and not in the package) and report errors in a debugger. If you run an application with those tests enabled and have no crashes, then they are not reporting any problems. 

If you do run into crashes, it will be necessary to run under a debugger, or pass the application to a developer to test more closely. 

*Why is fault injection not working?*

The fault injection probability was changed to parts per million in AppVerifier builds released after February 2007 based on customer feedback. So, a probability of 0n20000 is 2%, 0n500000 is 50% and so on.

!avrf –flt debugger extension can be used to change the probability on the fly in the debugger. However, the Low Resource Simulation check for the process should be turned on for this to work.

!avrf debugger extension is part exts.dll that ships with the debugger package. The changes in !avrf that support the probability change are in the latest debugger package. If you are experiencing problems with fault injection, please update your debuggers and the AppVerifier package.

*Why does Leak Verifier not report certain resource leaks?*

Leak Verifier does not report any resource leaks while a DLL or EXE module is loaded. When a module is unloaded, Leak Verifier issues a stop if any of the resources that were allocated by the module have not been released.

To inspect resources allocated by a loaded DLL or EXE, use the !avrf -leak debugger extension.

## See Also

[Application Verifier - Overview](application-verifier.md)

[Application Verifier - Features](application-verifier-features.md)

[Application Verifier - Testing Applications](application-verifier-testing-applications.md)
 
[Application Verifier - Tests within Application Verifier](application-verifier-tests-within-application-verifier.md)

[Application Verifier - Stop Codes and Definitions](application-verifier-stop-codes-and-definitions.md)

[Application Verifier - Debugging Application Verifier Stops](application-verifier-debugging-application-verifier-stops.md)