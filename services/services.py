import inetdServices
import timeSynchronization
import serviceClients
import networkConfiguration


def services_check():
    inetdServices.check_charge_services_not_enabled()
    inetdServices.check_daytime_services_not_enabled()
    inetdServices.check_discard_services_not_enabled()
    inetdServices.check_echo_services_not_enabled()
    inetdServices.check_time_services_not_enabled()
    inetdServices.check_tftp_server_not_enabled()
    inetdServices.check_xinetd_not_enabled()


def special_purpose_services_check():
    timeSynchronization.check_time_sync_is_used()
    timeSynchronization.check_ntp_configured()
    timeSynchronization.check_chrony_is_configured()
    timeSynchronization.check_x_window_system_not_installed()
    timeSynchronization.check_Avahi_server_not_enabled()
    timeSynchronization.check_CUPS_is_not_enabled()
    timeSynchronization.check_DHCP_server_is_not_enabled()
    timeSynchronization.check_LDAP_server_is_not_enabled()
    timeSynchronization.check_NFS_and_RPC_not_installed()
    timeSynchronization.check_DNS_server_not_enabled()
    timeSynchronization.check_ftp_server_not_enabled()
    timeSynchronization.check_http_server_not_enabled()
    timeSynchronization.check_IMAP_and_POP3_server_not_enabled()
    timeSynchronization.check_samba_is_not_enabled()
    timeSynchronization.check_http_proxy_is_not_enabled()
    timeSynchronization.check_SNMP_server_not_enabled()
    timeSynchronization.check_NIS_server_is_not_enabled()
    timeSynchronization.check_rsh_server_not_enabled()
    timeSynchronization.check_talk_server_is_not_enabled()
    timeSynchronization.check_telnet_server_not_enabled()
    timeSynchronization.check_tftp_server_not_enabled()
    timeSynchronization.check_rsync_server_is_not_enabled()


def service_clients_check():
    serviceClients.check_NIS_Client_not_installed()
    serviceClients.check_rsh_client_not_installed()
    serviceClients.check_talk_client_not_installed()
    serviceClients.check_telnet_client_not_installed()
    serviceClients.check_LDAP_client_not_installed()


def network_configuration_check():
    networkConfiguration.check_ip_forwarding_is_disabled()
    networkConfiguration.check_packet_redirect_sending_is_disabled()
    networkConfiguration.check_source_routed_packets_not_accepted()
    networkConfiguration.check_ICMP_redirects_are_not_accepted()
    networkConfiguration.check_secure_ICMP_redirect_are_not_accepted()
    networkConfiguration.check_suspicious_packets_are_logged()
    networkConfiguration.check_broadCast_ICMP_request_ignored()
    networkConfiguration.check_bogus_icmp_requests_ignored()
    networkConfiguration.check_reverse_path_filtering_enabled()
    networkConfiguration.check_tcp_SYN_cookies_is_enabled()
    networkConfiguration.check_IPv6_router_ads_not_accepted()
    networkConfiguration.check_IPv6_redirect_not_accepted()
    networkConfiguration.check_IPv6_is_disabled()


def run():
    #    services_check()
    #    special_purpose_services_check()
    #    service_clients_check()
    network_configuration_check()


run()
