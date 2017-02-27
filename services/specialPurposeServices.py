import source
import os

#----- 2.2.1.1 Ensure time synchronization is in use (Not Scored) -----#

def check_time_sync_is_used():

    config = '2.2.1.1 Ensure time synchronization is in use (Not Scored)'
    command1 = 'rpm -q ntp'
    command2 = 'rpm -q chrony'
    output = 'not installed'
    print('checking "'+ config +'" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()


    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output in terminal_output1 and output in terminal_output2:
        source.return_function(False,config)
    else:
        source.return_function(True,config)

# ----- 2.2.1.2 Ensure ntp is configured (Scored) -----#

def check_ntp_configured():

    config = '2.2.1.2 Ensure ntp is configured (Scored)'
    command1 = 'grep "^restrict" /etc/ntp.conf'
    output1 = 'restrict -4 default kod nomodify notrap nopeer noquery'
    output2 = 'restrict -6 default kod nomodify notrap nopeer noquery'

    print('checking "' + config + '" ..... ')


    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()


    if output1 in terminal_output1 and output2 in terminal_output1:
        source.return_function(True, config)
    else:
        source.return_function(False, config)

# --- 2.2.1.3 Ensure chrony is configured (Scored) --- #
def check_chrony_is_configured():

    config = '2.2.1.3 Ensure chrony is configured (Scored)'
    command1 = 'grep "^server" /etc/chrony.conf | wc -l'
    command2 = 'grep ^OPTIONS /etc/sysconfig/chronyd'
    output1 = 1
    output2 = 'OPTIONS="-u chrony"'

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read().split('\n')
    if int(terminal_output1[0]) > output1:
        result = True
    else:
        result = False

    terminal_variable = os.popen(command1)
    terminal_output2 = terminal_variable.read()

    if output2 in terminal_output2 and result:
        source.return_function(True,config)
    else:
        source.return_function(False,config)

#----- 2.2.2 Ensure X Window System is not installed (Scored) ----#

def check_x_window_system_not_installed():

    config = '2.2.2 Ensure X Window System is not installed (Scored)'
    command = 'rpm -qa xorg-x11*'
    output = ''
    source.output_isEqualTo_terminal_output(config,command,output)

# ---- 2.2.3 Ensure Avahi Server is not enabled (Scored) --- #

def check_Avahi_server_not_enabled():

    config = '2.2.3 Ensure Avahi Server is not enabled (Scored)'
    command = 'systemctl is-enabled avahi-daemon'
    output = 'disabled'
    source.output_isIn_terminal_output(config,command,output)

# ---- 2.2.4 Ensure CUPS is not enabled (Scored) ---- #

def check_CUPS_is_not_enabled():

    config = '2.2.4 Ensure CUPS is not enabled (Scored)'
    command = 'systemctl is-enabled cups'
    output = 'disabled'
    source.output_isIn_terminal_output(config,command,output)

#---- 2.2.5 Ensure DHCP Server is not enabled (Scored) -----#

def check_DHCP_server_is_not_enabled():


    config = '2.2.5 Ensure DHCP Server is not enabled (Scored)'
    command = 'systemctl is-enabled dhcpd'
    output = 'disabled'
    source.output_isIn_terminal_output(config,command,output)

# ---- 2.2.6 Ensure LDAP server is not enabled (Scored) ---- #

def check_LDAP_server_is_not_enabled():

    config = '2.2.6 Ensure LDAP server is not enabled (Scored)'
    command = 'systemctl is-enabled slapd'
    output = 'disabled'
    source.output_isIn_terminal_output(config,command,output)

# --- 2.2.7 Ensure NFS and RPC are not enabled (Scored) ---#

def check_NFS_and_RPC_not_installed():

    config = '2.2.7 Ensure NFS and RPC are not enabled (Scored)'
    command1 = 'systemctl is-enabled nfs'
    command2 = 'systemctl is-enabled rpcbind'
    output = 'disabled'

    print('checking "' + config + '" ..... ')


    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output in terminal_output1 and output in terminal_output1:
        source.return_function(True, config)
    else:
        source.return_function(False, config)