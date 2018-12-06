---
title: Cross Machine Execution
description: Cross Machine Execution
ms.assetid: FDDD2320-E853-45a8-9820-12FB16365B9C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cross Machine Execution


TAEF supports the ability to execute Te.exe on one machine but run the tests on a separate machine. TAEF authenticates, authorizes, and deploys the necessary binaries to execute the tests and logs all information back to the originating console.

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


The following requirements are necessary in order to execute tests remotely:

-   You must install and run [Te.Service](te-service.md) (either x86 or x64) on **the target machine**.

### <span id="Executing_with_domain_accounts"></span><span id="executing_with_domain_accounts"></span><span id="EXECUTING_WITH_DOMAIN_ACCOUNTS"></span>Executing with domain accounts

-   The domain account must be an administrator or a member of the local "Remote TAEF Users" group on the target machine.

### <span id="Executing_with_non-domain_accounts"></span><span id="executing_with_non-domain_accounts"></span><span id="EXECUTING_WITH_NON-DOMAIN_ACCOUNTS"></span>Executing with non-domain accounts

-   The local (non-domain account) must exist with the same user name and password on both machines.
-   That user must be a member of the local "Remote TAEF Users" group on the target machine.
-   On the host machine, the local user can execute Te.exe, or, alternately, you may add generic credentials for the local user to the credential manager.

    ``` syntax
    cmdkey /generic:<targetmachine> /user:<user_name> /pass:<password>
    ```

-   If you are running on a domain-joined machine, the domain-joined machine must have an IPSec boundary exclusion.

## <span id="Executing_Tests_Remotely"></span><span id="executing_tests_remotely"></span><span id="EXECUTING_TESTS_REMOTELY"></span>Executing Tests Remotely


### <span id="_runOn_"></span><span id="_runon_"></span><span id="_RUNON_"></span>/runOn:

In order to run tests remotely, you must specify the **/runOn:&lt;machine name&gt;** parameter to Te.exe along with the rest of your commands. If you meet the prerequisites, the rest of the user experience will be identical to that found when executing tests locally. All log output will be saved/written to the local machine.

For example:

``` syntax
te unittests\wex.common.tests.dll /runon:TAEFTest1
```

-   Sends all necessary binaries for your test to the target machine (TAEFTest1) and remotely executes all TAEF tests that exist within wex.common.tests.dll, while logging back to your console.

If you fail to connect to the remote machine due to HRESULT 0x800706BA and you are sure that you spelled the machine name correctly, try using the machine's IP address or using the **/disableTimeouts** switch. Sometimes the DNS delay can be large enough to cause the connection attempt to time out.

**Note:** If this is the first time specifying the **/runOn:** command, you may need to click **Unblock** on a firewall exclusion dialog for Te.exe.

### <span id="Test_Dependencies"></span><span id="test_dependencies"></span><span id="TEST_DEPENDENCIES"></span>Test Dependencies

Te.exe automatically determines all of your test's native and managed module dependencies and sends them to the remote machine along with your test dll. This excludes *system* binaries as well as any COM libraries that your test requires.

You can manually specify additional test dependencies via the **/TestDependencies** command line parameter in the form of a semicolon-delimited list of files or directories to copy.

- **Files**

  Each file specification can contain wildcard characters (test.txt; test\*.dll; etc.). For example:

  ``` syntax
  te unittests\wex.common.tests.dll /runon:TAEFTest1 /TestDependencies:*verification*.jpg;mysample.txt
  ```
  -   Sends all necessary binaries for your test to TAEFTest1 as well as any files found that match the files specified in the **/TestDependencies** parameter.
- **Directories**

  TAEF supports recursive directory searches for directories that exist *at or below* the directory that contains the test binary. For example:

  ``` syntax
  te unittests\wex.common.tests.dll /runon:TAEFTest1 /TestDependencies:unittests\...
  ```

  -   Sends all necessary binaries for your test to TAEFTest1 as well as all files/directories within or below the *unittests* directory. TAEF retains the directory hierarchy.

  ``` syntax
  _    te unittests\wex.common.tests.dll /runon:TAEFTest1 /TestDependencies:unittests\*.jpg...
  ```

  -   Sends all necessary binaries for your test to TAEFTest1 as well as all jpg files within or below the *unittests* directory. TAEF retains the directory hierarchy.

  <strong>Note:</strong>If you specify a recursive or non-recursive directory search for a directory that does not exist *at or below* the test directory, all files will be copied to the remote machine but the directory hierarchy will be flattened.

You can aso specify test dependencies via [DeploymentItem metadata](deploymentitem-metadata.md)

## User Context 


By default, TAEF attempts to run the tests on the remote machine with your user context. It does so by:

-   Enumerating all active sessions on the remote machine and looking for a session that is owned by you.
    -   If TAEF finds a session that is owned by you on the remote machine, it runs the tests in that session (on that desktop, etc.).

        **Note:** This won't necessarily be the console session. It could be a remote desktop session.

    -   If TAEF **does not find** a session that is owned by you on the remote machine, it runs the tests as the user who is logged into the console session (on that desktop, etc.).
    -   Finally, if you do not own a session on the remote machine and no one is logged into the console session, TAEF will run the tests in session 0 (non-interactive).

### <span id="RunAs"></span><span id="runas"></span><span id="RUNAS"></span>RunAs

If you specify a [/runAs](runas.md) value in addition to **/runOn**, TAEF uses the above heuristics in addition to those that are necessary to fulfill the **/runAs** setting. For example:

``` syntax
te unittests\wex.common.tests.dll /runon:TAEFTest1 /runas:system
```

-   Executes all TAEF tests that exist within wex.common.tests.dll on TAEFTest1 with the system account.

## <span id="How_It_Works"></span><span id="how_it_works"></span><span id="HOW_IT_WORKS"></span>How It Works


-   Te.exe connects to the instance of Te.Service that is running on the remote machine
    -   Windows authentication (Negotiate) authenticates you with the Te.Service.
    -   The Te.Service authorizes you by verifying that you are an administrator or a member of the local "Remote TAEF Users" group on the remote machine.
-   Te.Service creates a directory under *RemoteTests*, with the same name as the test dll.
-   Te.exe builds a list of files that are necessary to execute your tests on the remote machine. This list includes:
    -   The necessary TAEF binaries
    -   All native and/or managed binary dependencies for your test dll (excluding system binaries)
    -   Any additional files that are specified by you in the **/TestDependencies** parameter
-   Te.exe sends the test dependency list, along with the CRCs for each file, to Te.Service.
-   Te.Service looks for each file on the remote machine and compares the CRC values. Any matches are removed from the list, and the list is sent back to the client.
-   If there are any files left in the dependency list, Te.exe sends each dependency to Te.Service.
    -   Te.Service saves them in the &lt;Te.Service directory&gt;\\RemoteTests\\&lt;test dll name&gt; directory.
-   Te.exe asks Te.Service to launch a new Te.ProcessHost.exe instance on the remote machine using the correct [user context](#user-context).
-   Te.exe connects to the remote Te.ProcessHost.exe instance and begins executing the tests.

 

 





