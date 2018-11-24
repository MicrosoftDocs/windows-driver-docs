---
title: RunFixtureAs
description: TAEF provides a mechanism to execute test fixtures within a different context than their corresponding tests.
ms.assetid: FAFF5265-5268-412E-86A5-149B187B1376
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RunFixtureAs


TAEF uses RunFixtureAs to execute test fixtures (module, class, and test-level setup and cleanup functions) in a context other than the corresponding test(s).

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


-   [Te.Service](te-service.md) must be installed and running on the machine in order to run elevated test fixtures from a non-elevated Te.exe process, or to run test fixtures as Local System.

## <span id="Overview"></span><span id="overview"></span><span id="OVERVIEW"></span>Overview


RunFixtureAs can be applied at the module, class, and or test level, and will be inherited down the test tree. In order to support the ability to opt out of RunFixtureAs inheritance at a given level in the tree, RunFixtureAs:\[scope\] metadata is also supported.

For example, if a module is marked with RunFixtureAs=System, a class (ClassA) can be marked as RunFixtureAs:Test=Default. In such a case, the module and class fixtures will run as System, but the test-level fixtures within ClassA will be run in the same context as Te.exe (although still in a different process than the test).

The RunFixtureAs:\[scope\] metadata value is not inherited down the test tree; it only applies to the specified scope.

## <span id="Deterministic_Guarantees"></span><span id="deterministic_guarantees"></span><span id="DETERMINISTIC_GUARANTEES"></span>Deterministic Guarantees


-   By default (if no RunFixtureAs values are specified), tests and fixtures are guaranteed to run within the same process.
-   If a fixture is marked with a valid RunFixtureAs value other than 'Test', the fixture will be run in a different process than the test. This means that even if a test is marked with RunAs=Elevated and RunFixtureAs=Elevated, the test will run in an elevated process, and its fixtures will run in a separate elevated process.
-   Matching fixture pairs for a given scope will always be run within the same process (for example, a class's setup and cleanup fixtures will be run within the same process).

## <span id="RunFixtureAs_Types_"></span><span id="runfixtureas_types_"></span><span id="RUNFIXTUREAS_TYPES_"></span>RunFixtureAs Types


TAEF supports the following RunFixtureAs types, which are specified by the test metadata:

<span id="System"></span><span id="system"></span><span id="SYSTEM"></span>**System**  
TAEF runs the fixture as Local System.

**Note**  The test fixtures that you run as Local System should not create any UI. If your fixtures need to create or interact with UI, you need to move your UI-related code into separate executables that are launched on a desktop from your tests using CreateProcessAsUser.

 

<span id="Elevated"></span><span id="elevated"></span><span id="ELEVATED"></span>**Elevated**  
TAEF ensures that the fixture is run in an elevated process by spawning an elevated process in which to run the fixture if necessary.

**Note**  The user executing TAEF must be a member of the administrators group in order to execute fixtures marked with RunFixtureAs=Elevated. This is due to the fact that non-administrators do not have a split token to elevate.

 

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default**  
TAEF runs the fixture in the same context as Te.exe (but still within a different process than the test).

<span id="Broker"></span><span id="broker"></span><span id="BROKER"></span>**Broker**  
TAEF runs the fixture in an 'Immersive Broker' process.

**Note**  
-   'Broker' is only supported on Windows 8 and higher operating systems.
-   The test signing policy must be enabled on the system. For more information, [The TESTSIGNING Boot Configuration Option](https://msdn.microsoft.com/library/windows/hardware/ff553484).
-   Running tests remotely with 'RunFixtureAs=Broker' is not currently supported.
-   When executing with 'RunFixtureAs=Broker' TAEF will use the "TE.ProcessHost.Broker.exe" process for fixture execution, not "TE.ProcessHost.exe".

 

<span id="UIAccess"></span><span id="uiaccess"></span><span id="UIACCESS"></span>**UIAccess**  
TAEF runs the fixture in a process marked-up with the UIAccess execution level. For information on UIAccess for UI automation applications, see the [Windows Integrity Mechanism Design](https://msdn.microsoft.com/library/bb625963).

**Note**  
-   UIAccess is only supported on Vista and higher operating systems.
-   The TAEF binaries must be running from a folder under the Program Files folder on the computer.
-   Running tests remotely with 'RunFixtureAs=UIAccess' is not currently supported.
-   When executing with 'RunFixtureAs=UIAccess' TAEF will use the "TE.ProcessHost.UIAccess.exe" process for fixture execution, not "TE.ProcessHost.exe".

 

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test**  
TAEF runs the fixture in the same process or context as the test.

**Note**  This is the default TAEF behavior when no RunFixtureAs settings are specified.

 

## <span id="RunFixtureAs__scope_"></span><span id="runfixtureas__scope_"></span><span id="RUNFIXTUREAS__SCOPE_"></span>RunFixtureAs:\[scope\]


TAEF supports the following RunFixtureAs:\[scope\] values, which are specified by the test metadata.

<span id="RunFixtureAs_Module__RunFixtureAs_Assembly__or_RunFixtureAs_Dll"></span><span id="runfixtureas_module__runfixtureas_assembly__or_runfixtureas_dll"></span><span id="RUNFIXTUREAS_MODULE__RUNFIXTUREAS_ASSEMBLY__OR_RUNFIXTUREAS_DLL"></span>**RunFixtureAs:Module**, **RunFixtureAs:Assembly**, or **RunFixtureAs:Dll**  
The RunFixtureAs value will apply only to the Module level node in the test hierarchy.

<span id="RunFixtureAs_Class"></span><span id="runfixtureas_class"></span><span id="RUNFIXTUREAS_CLASS"></span>**RunFixtureAs:Class**  
The RunFixtureAs value will apply only to the Class level nodes in the test hierarchy.

<span id="RunFixtureAs_Method_or_RunFixtureAs_Test"></span><span id="runfixtureas_method_or_runfixtureas_test"></span><span id="RUNFIXTUREAS_METHOD_OR_RUNFIXTUREAS_TEST"></span>**RunFixtureAs:Method** or **RunFixtureAs:Test**  
The RunFixtureAs value will apply only to the Test level nodes in the test hierarchy.

## <span id="Marking_Tests_with_RunFixtureAs"></span><span id="marking_tests_with_runfixtureas"></span><span id="MARKING_TESTS_WITH_RUNFIXTUREAS"></span>Marking Tests with RunFixtureAs


```ManagedCPlusPlus
MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
        TEST_METHOD_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestSetup and MyTestCleanup run as Elevated
-   MyClassSetup and MyClassCleanup run as System (within the same process as MyTestMethod)
-   MyModuleSetup and MyModuleCleanup run as System (within the same process as MyTestMethod)

```ManagedCPlusPlus
MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestSetup and MyTestCleanup run as Elevated
-   MyClassSetup and MyClassCleanup run as Elevated
-   MyModuleSetup and MyModuleCleanup run as System (within the same process as MyTestMethod)

```ManagedCPlusPlus
MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"System")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
        TEST_METHOD_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as Restricted
-   MyTestSetup and MyTestCleanup run as Elevated
-   MyClassSetup and MyClassCleanup run as System
-   MyModuleSetup and MyModuleCleanup run as Restricted (within the same process as MyTestMethod)

```ManagedCPlusPlus
MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"System")
        TEST_METHOD_PROPERTY(L"RunFixtureAs:Test", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run as Elevated; the RunFixtureAs:Test scoping applied to all test methods within the MyTests class
-   MyClassSetup and MyClassCleanup run as System (within a different process than MyTestMethod)
-   MyModuleSetup and MyModuleCleanup run as within the context of their respective test process (System for MyTestMethod and Restricted for MyTestMethod2)

```ManagedCPlusPlus
MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"System")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
        TEST_METHOD_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run as System for MyTestMethod and as Elevated for MyTestMethod2
-   MyClassSetup and MyClassCleanup run as System (within a different process than MyTestMethod)
-   MyModuleSetup and MyModuleCleanup run as within the context of their respective test process (System for MyTestMethod and Restricted for MyTestMethod2)

```ManagedCPlusPlus
BEGIN_MODULE()
    MODULE_PROPERTY(L"RunFixtureAs", L"System")
END_MODULE()

MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"Default")
        TEST_CLASS_PROPERTY(L"RunFixtureAs:Test", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run as Elevated for both MyTestMethod and MyTestMethod2
-   MyClassSetup and MyClassCleanup run as Default (within the same context as Te.exe is currently running, yet within a different process than MyTestMethod and MyTestMethod2)
-   MyModuleSetup and MyModuleCleanup run as System (within a different process than MyTestMethod)

```ManagedCPlusPlus
BEGIN_MODULE()
    MODULE_PROPERTY(L"RunFixtureAs", L"System")
    MODULE_PROPERTY(L"RunFixtureAs:Test", L"Test")
END_MODULE()

MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run within the same process as MyTestMethod and MyTestMethod2
-   MyClassSetup and MyClassCleanup run as Elevated
-   MyModuleSetup and MyModuleCleanup run as System (within a different process than MyTestMethod)

```ManagedCPlusPlus
BEGIN_MODULE()
    MODULE_PROPERTY(L"RunFixtureAs", L"System")
    MODULE_PROPERTY(L"RunFixtureAs:Test", L"Test")
END_MODULE()

MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
        TEST_METHOD_PROPERTY(L"RunFixtureAs", L"Elevated")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The preceding example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run within the same process as MyTestMethod and in an Elevated process for MyTestMethod2
-   MyClassSetup and MyClassCleanup run as Elevated
-   MyModuleSetup and MyModuleCleanup run as System (within a different process than MyTestMethod)

```ManagedCPlusPlus
BEGIN_MODULE()
    MODULE_PROPERTY(L"RunFixtureAs", L"System")
END_MODULE()

MODULE_SETUP(MyModuleSetup);
MODULE_CLEANUP(MyModuleCleanup);

class MyTests
{
    BEGIN_TEST_CLASS(MyTests)
        TEST_CLASS_PROPERTY(L"RunFixtureAs:Class", L"Elevated")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTestMethod)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()

    BEGIN_TEST_METHOD(MyTestMethod2)
        TEST_METHOD_PROPERTY(L"RunAs", L"Restricted")
    END_TEST_METHOD()

    TEST_METHOD_SETUP(MyTestSetup);
    TEST_METHOD_CLEANUP(MyTestCleanup);

    TEST_CLASS_SETUP(MyClassSetup);
    TEST_CLASS_CLEANUP(MyClassCleanup);
};
```

The above example will run tests and fixtures as follows:

-   MyTestMethod runs as System
-   MyTestMethod2 runs as Restricted
-   MyTestSetup and MyTestCleanup run as System (within a different process than MyTestMethod)
-   MyClassSetup and MyClassCleanup run as Elevated
-   MyModuleSetup and MyModuleCleanup run as System (within a different process than MyTestMethod)

 

 





