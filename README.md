# Redhat7-CIS-Assessment-tool

what is NOT included?

- 1.1.18 Ensure nodev option set on removable media partitions (Not
Scored)

- 1.1.19 Ensure nosuid option set on removable media partitions (Not
Scored)

- 1.1.20 Ensure noexec option set on removable media partitions (Not
Scored)

- 1.2.1 Ensure package manager repositories are configured (Not Scored)
this requires careful auditing by system administrator
run #yum repolist
and check the output

-1.2.3 Ensure GPG keys are configured (Not Scored)

-1.2.4 Ensure Red Hat Network or Subscription Manager connection is
configured (Not Scored)

-1.3.2 Ensure filesystem integrity is regularly checked (Scored)



- 1.7.1.1 Ensure message of the day is configured properly (Scored)


included but requires sudo rights
-1.4.1 Ensure permissions on bootloader config are configured (Scored) - requires root access

-1.4.2 Ensure bootloader password is set (Scored) - requires root access

-1.6.1.1 Ensure SELinux is not disabled in bootloader configuration