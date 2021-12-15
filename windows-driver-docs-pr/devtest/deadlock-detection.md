---
title: Deadlock Detection
description: Deadlock Detection
keywords:
- Deadlock Detection feature WDK Driver Verifier
- deadlocks WDK Driver Verifier
- locked resources WDK Driver Verifier
- thread locks WDK Driver Verifier
ms.date: 06/04/2020
---

# Deadlock Detection

Deadlock Detection monitors the driver's use of resources which need to be locked -- spin locks, mutexes, and fast mutexes. This Driver Verifier option will detect code logic that has the potential to cause a deadlock at some future point.

The Deadlock Detection option of Driver Verifier, along with the **!deadlock** kernel debugger extension, is an effective tool for making sure your code avoids poor use of these resources.

Deadlock Detection is supported only in Windows XP and later versions of Windows.

## Causes of Deadlocks

A *deadlock* is caused when two or more threads come into conflict over some resource, in such a way that no execution is possible.

The most common form of deadlock occurs when two or more threads wait for a resource that is owned by the other thread. This is illustrated as follows:

| Thread 1 | Thread 2 |
| --- | --- |
| Takes Lock A | Takes Lock B |
| Requests Lock B | Requests Lock A |

If both sequences happen at the same time, Thread 1 will never get Lock B because it is owned by Thread 2, and Thread 2 will never get Lock A because it is owned by Thread 1. At best this causes the threads involved to halt, and at worst causes the system to stop responding.

Deadlocks are not limited to two threads and two resources. Three-way deadlocks between three threads and three locks are common -- and even five-part or six-part deadlocks occur occasionally. These deadlocks require a certain degree of "bad luck" since they rely on a number of things happening simultaneously. However, the farther apart the lock acquisitions are, the more likely these become.

Single-thread deadlocks can occur when a thread attempts to take a lock that it already owns.

The common denominator among all deadlocks is that lock hierarchy is not respected. Whenever it is necessary to have more than one lock acquired at a time, each lock should have a clear precedence. If A is taken before B at one point and B before C at another, the hierarchy is A-B-C. This means that A must never be acquired after B or C, and B must not be acquired after C.

Lock hierarchy should be followed even when there is no possibility of a deadlock, since in the process of maintaining the code it will be easy for a deadlock to be accidentally introduced.

## Resources That Can Cause Deadlocks

The most unambiguous deadlocks are the result of *owned* resources. These include spin locks, mutexes, fast mutexes, and ERESOURCEs.

Resources that are signaled rather than acquired (such as events and LPC ports) tend to cause much more ambiguous deadlocks. It is of course possible, and all too common, for code to misuse these resources in such a way that two threads will end up waiting indefinitely for each other to complete. However, since these resources are not actually owned by any one thread, it is not possible to identify the delinquent thread with any degree of certainty.

The Deadlock Detection option of Driver Verifier looks for potential deadlocks involving spin locks, mutexes, and fast mutexes. It does not monitor the use of ERESOURCEs, nor does it monitor the use of nonowned resources.

## Effects of Deadlock Detection

Driver Verifier's Deadlock Detection routines find lock hierarchy violations that are not necessarily simultaneous. Most of the time, these violations identify code paths that will deadlock when given the chance.

To find potential deadlocks, Driver Verifier builds a graph of resource acquisition order and checks for loops. If you were to create a node for each resource, and draw an arrow any time one lock is acquired before another, then path loops would represent lock hierarchy violations.

Driver Verifier will issue a bug check when one of these violations is discovered. This will happen before any actual deadlocks occur.

> [!NOTE]
> Even if the conflicting code paths can never happen simultaneously, they should still be rewritten if they involve lock hierarchy violations. Such code is a "deadlock waiting to happen" that could cause real deadlocks if the code is rewritten slightly.

When Deadlock Detection finds a violation, it will issue bug check 0xC4. The first parameter of this bug check will indicate the exact violation. Possible violations include:

-   Two or more threads involved in a lock hierarchy violation

-   A thread that tries to exclusively acquire a resource for which it is already a shared owner (exclusively owned resources can be acquired shared; shared resources cannot be acquired exclusively).

- A thread that tries to acquire the same resource twice (a self-deadlock)

- A resource that is released without having been acquired first

- A resource that is released by a different thread than the one that acquired it

- A resource that is initialized more than once, or not initialized at all

- A thread that is deleted while still owning resources

- Starting in Windows 7, Driver Verifier can predict possible deadlocks. For example, trying to use the same KSPIN\_LOCK data structure both as a regular spin lock and as a stack queued spin lock.

See [**Bug Check 0xC4**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION) for a list of the bug check parameters.

## Monitoring Deadlock Detection

Once Deadlock Detection finds a violation, the **!deadlock** kernel debugger extension can be used to investigate exactly what has occurred. It can display the lock hierarchy topology as well as the call stacks for each thread at the time the locks were originally acquired.

There is a detailed example of the [**!deadlock**](../debugger/-deadlock.md) extension, as well as general information about debugger extensions, in the documentation in the Debugging Tools for Windows package. See [Windows Debugging](../debugger/index.md) for details.

### Activating This Option

> [!NOTE]
> This option is incompatible with [Kernel synchronization delay fuzzing](./kernel-synchronization-delay-fuzzing.md)

You can activate the Deadlock Detection feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

- **At the command line**

    At the command line, the Deadlock Detection option is represented by **Bit 5 (0x20)**. To activate Deadlock Detection, use a flag value of 0x20 or add 0x20 to the flag value. For example:

    ```console
    verifier /flags 0x20 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows Vista and later versions of Windows, you can also activate and deactivate Deadlock Detection without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```console
    verifier /volatile /flags 0x20 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Deadlock Detection feature is also included in the standard settings. For example:

    ```console
    verifier /standard /driver MyDriver.sys
    ```

- **Using Driver Verifier Manager**

    1. Select **Create custom settings (for code developers)** and then select **Next**.

    1. Select **Select individual settings from a full list**.

    1. Select (check) **Deadlock detection**.

The Deadlock Detection feature is also included in the standard settings. To use this feature, in **Driver Verifier Manager**, select **Create Standard Settings**.
