data = """source_ip dest_ip dest_port BLOCK/ALLOW
source_ip dest_ip dest_port BLOCK/ALLOW
0.0.0.0/0                10.55.163.0/24              ALL                     BLOCK
10.55.163.0/24           0.0.0.0/0                   ALL                     ALLOW
0.0.0.0/0                10.55.163.141               443/tcp                 ALLOW
0.0.0.0/0                10.55.163.141               6443/tcp                ALLOW
0.0.0.0/0                10.55.163.141               80/tcp                  ALLOW
10.55.53.0/24            10.55.163.141               12200/udp               ALLOW
10.55.54.0/24            10.55.163.141               12200/udp               ALLOW
10.55.8.192/26           10.55.163.141               12200/udp               ALLOW
10.55.63.192/26          10.55.163.141               12200/udp               ALLOW
10.55.53.0/24            10.55.163.141               12201/udp               ALLOW
10.55.54.0/24            10.55.163.141               12201/udp               ALLOW
10.55.8.192/26           10.55.163.141               12201/udp               ALLOW
10.55.63.192/26          10.55.163.141               12201/udp               ALLOW
10.89.213.10/32          10.55.163.141               3304/tcp                ALLOW
10.89.213.19/32          10.55.163.141               3304/tcp                ALLOW
10.106.22.2/32           10.55.163.141               3305/tcp                ALLOW
10.106.22.4/32           10.55.163.141               3305/tcp                ALLOW
131.237.94.132/32        10.55.163.141               3305/tcp                ALLOW
10.112.10.16/32          10.55.163.141               3306/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3306/tcp                ALLOW
10.112.10.53/32          10.55.163.141               3307/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3307/tcp                ALLOW
10.124.20.2/32           10.55.163.141               3308/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3308/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3309/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3310/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3311/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3312/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3313/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3314/tcp                ALLOW
10.113.65.131/32         10.55.163.141               3315/tcp                ALLOW
10.113.66.190/32         10.55.163.141               3315/tcp                ALLOW
10.113.96.198/32         10.55.163.141               3315/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3315/tcp                ALLOW
10.113.99.139/32         10.55.163.141               3315/tcp                ALLOW
10.55.40.192/26          10.55.163.141               3315/tcp                ALLOW
10.55.6.192/26           10.55.163.141               3315/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3315/tcp                ALLOW
131.237.94.132/32        10.55.163.141               3315/tcp                ALLOW
145.31.254.93/32         10.55.163.141               3315/tcp                ALLOW
0.0.0.0/0                10.55.163.141               3316/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3317/tcp                ALLOW
10.113.66.190/32         10.55.163.141               3317/tcp                ALLOW
10.113.99.139/32         10.55.163.141               3317/tcp                ALLOW
10.114.234.0/24          10.55.163.141               3371/tcp                ALLOW
10.55.8.192/26           10.55.163.141               3375/tcp                ALLOW
10.55.54.192/26          10.55.163.141               3375/tcp                ALLOW
10.55.53.0/24            10.55.163.141               3378/tcp                ALLOW
10.55.54.192/26          10.55.163.141               3379/tcp                ALLOW
10.55.54.192/26          10.55.163.141               3380/tcp                ALLOW
10.55.8.192/26           10.55.163.141               3379/tcp                ALLOW
10.55.8.192/26           10.55.163.141               3380/tcp                ALLOW
10.114.242.73/32         10.55.163.141               3388/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3390/tcp                ALLOW
145.31.254.29/32         10.55.163.141               3390/tcp                ALLOW
145.31.254.105/32        10.55.163.141               3391/tcp                ALLOW
145.31.254.138/32        10.55.163.141               3391/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3391/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3392/tcp                ALLOW
35.205.122.156/32        10.55.163.141               3392/tcp                ALLOW
145.31.255.1/32          10.55.163.141               3393/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3393/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3394/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3395/tcp                ALLOW
10.0.23.89/32            10.55.163.141               3395/tcp                ALLOW
185.34.169.200/32        10.55.163.141               3395/tcp                ALLOW
10.55.53.0/24            10.55.163.141               3396/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3396/tcp                ALLOW
10.55.9.192/26           10.55.163.141               3396/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3397/tcp                ALLOW
149.249.250.129/32       10.55.163.141               3397/tcp                ALLOW
10.112.10.16/32          10.55.163.141               3406/tcp                ALLOW
10.112.10.53/32          10.55.163.141               3407/tcp                ALLOW
10.124.20.2/32           10.55.163.141               3408/tcp                ALLOW
10.113.65.131/32         10.55.163.141               3415/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3415/tcp                ALLOW
145.31.254.93/32         10.55.163.141               3415/tcp                ALLOW
10.113.65.130/32         10.55.163.141               3415/tcp                ALLOW
10.55.40.192/26          10.55.163.141               3415/tcp                ALLOW
10.55.6.192/26           10.55.163.141               3415/tcp                ALLOW
10.113.66.190/32         10.55.163.141               3415/tcp                ALLOW
10.113.65.131/32         10.55.163.141               3417/tcp                ALLOW
10.113.66.190/32         10.55.163.141               3417/tcp                ALLOW
10.89.2.8/32             10.55.163.141               3420/tcp                ALLOW
10.89.2.10/32            10.55.163.141               3420/tcp                ALLOW
10.89.2.8/32             10.55.163.141               3421/tcp                ALLOW
10.89.2.10/32            10.55.163.141               3421/tcp                ALLOW
10.89.2.8/32             10.55.163.141               3422/tcp                ALLOW
10.89.2.10/32            10.55.163.141               3422/tcp                ALLOW
10.106.26.1/32           10.55.163.141               3440/tcp                ALLOW
10.106.26.2/32           10.55.163.141               3440/tcp                ALLOW
10.106.26.1/32           10.55.163.141               3441/tcp                ALLOW
10.106.26.2/32           10.55.163.141               3441/tcp                ALLOW
10.106.26.1/32           10.55.163.141               3442/tcp                ALLOW
10.106.26.2/32           10.55.163.141               3442/tcp                ALLOW
10.89.213.10/32          10.55.163.141               3450/tcp                ALLOW
10.89.213.19/32          10.55.163.141               3450/tcp                ALLOW
10.89.213.10/32          10.55.163.141               3451/tcp                ALLOW
10.89.213.19/32          10.55.163.141               3451/tcp                ALLOW
10.89.213.10/32          10.55.163.141               3452/tcp                ALLOW
10.89.213.19/32          10.55.163.141               3452/tcp                ALLOW
10.106.22.2/32           10.55.163.141               3460/tcp                ALLOW
10.106.22.4/32           10.55.163.141               3460/tcp                ALLOW
10.106.22.2/32           10.55.163.141               3461/tcp                ALLOW
10.106.22.4/32           10.55.163.141               3461/tcp                ALLOW
10.106.22.2/32           10.55.163.141               3462/tcp                ALLOW
10.106.22.4/32           10.55.163.141               3462/tcp                ALLOW
10.116.196.0/24          10.55.163.141               3471/tcp                ALLOW
10.55.8.192/26           10.55.163.141               3475/tcp                ALLOW
10.55.8.192/26           10.55.163.141               3479/tcp                ALLOW
10.55.54.192/26          10.55.163.141               3475/tcp                ALLOW
10.55.54.192/26          10.55.163.141               3479/tcp                ALLOW
10.117.179.142/32        10.55.163.141               3488/tcp                ALLOW
10.117.179.155/32        10.55.163.141               3488/tcp                ALLOW
145.31.254.29/32         10.55.163.141               3490/tcp                ALLOW
145.31.254.105/32        10.55.163.141               3491/tcp                ALLOW
145.31.254.138/32        10.55.163.141               3491/tcp                ALLOW
35.205.122.156/32        10.55.163.141               3492/tcp                ALLOW
145.31.255.1/32          10.55.163.141               3493/tcp                ALLOW
10.0.23.90/32            10.55.163.141               3495/tcp                ALLOW
185.34.169.198/32        10.55.163.141               3495/tcp                ALLOW
149.249.250.129/32       10.55.163.141               3497/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3115/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3115/tcp                ALLOW
131.237.94.132/32        10.55.163.141               3115/tcp                ALLOW
10.31.45.109/32          10.55.163.141               3116/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3117/tcp                ALLOW
10.31.45.109/32          10.55.163.141               3118/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3119/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3215/tcp                ALLOW
10.48.106.250/32         10.55.163.141               3215/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3215/tcp                ALLOW
131.237.94.132/32        10.55.163.141               3215/tcp                ALLOW
0.0.0.0/0                10.55.163.141               3216/tcp                ALLOW
10.113.97.251/32         10.55.163.141               3217/tcp                ALLOW
10.55.7.192/26           10.55.163.141               3178/tcp                ALLOW
10.55.9.192/26           10.55.163.141               3178/tcp                ALLOW
10.55.53.192/26          10.55.163.141               3178/tcp                ALLOW
10.55.63.192/26          10.55.163.141               3178/tcp                ALLOW
10.55.7.192/26           10.55.163.141               3278/tcp                ALLOW
10.55.9.192/26           10.55.163.141               3278/tcp                ALLOW
10.55.53.192/26          10.55.163.141               3278/tcp                ALLOW
10.55.63.192/26          10.55.163.141               3278/tcp                ALLOW
10.55.7.192/26           10.55.163.141               3378/tcp                ALLOW
10.55.9.192/26           10.55.163.141               3378/tcp                ALLOW
10.55.53.192/26          10.55.163.141               3378/tcp                ALLOW
10.55.63.192/26          10.55.163.141               3378/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3190/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3191/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3192/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3193/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3194/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3195/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3196/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3197/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3198/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3199/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3101/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3290/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3291/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3292/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3293/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3294/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3295/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3296/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3297/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3298/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3299/tcp                ALLOW
10.74.85.2/32            10.55.163.141               3201/tcp                ALLOW
10.113.99.139            10.55.163.141               3117/tcp                ALLOW
10.113.99.139            10.55.163.141               3119/tcp                ALLOW
10.113.99.139            10.55.163.141               3217/tcp                ALLOW
10.113.99.139            10.55.163.141               3115/tcp                ALLOW
10.113.99.139            10.55.163.141               3215/tcp                ALLOW
"""


# ports = [3115, 3116, 3117, 3118, 3119, 3201, 3215, 3216, 3217, 3278, 3315, 3317, 3208, 12200, 12201, 3408]

def first_part():
    return """resource "nsxt_policy_gateway_policy" "gateway_policy" {
  display_name    = "${var.env_name}-gateway-policy"
  category        = "LocalGatewayRules"
  locked          = false
  sequence_number = 1
  stateful        = true
  tcp_strict      = false

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }

  dynamic "rule" {
    for_each = local.standard_ports ? [""] : []
    content {
      display_name       = "allow-standard-ports"
      action             = "ALLOW"
      direction          = "IN_OUT"
      ip_version         = "IPV4_IPV6"
      services           = [nsxt_policy_service.standard_ports_service[0].path]
      destination_groups = ["${var.k8s_lb_public_ip}"]
      scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
    }
  }

  rule {
    display_name  = "allow-all-internal"
    action        = "ALLOW"
    direction     = "IN_OUT"
    ip_version    = "IPV4_IPV6"
    source_groups = ["${var.network_cidr}"]
    scope         = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
  }

  rule {
    display_name       = "allow-ssh"
    action             = "ALLOW"
    direction          = "IN_OUT"
    ip_version         = "IPV4_IPV6"
    destination_groups = ["${var.jumpbox_public_ip}", "${var.dns_instance_public_ip}"]
    services           = [nsxt_policy_service.ssh_port_service.path]
    scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
  }

  dynamic "rule" {
    for_each = local.ports_3190_3199 ? [""] : []
    content {
      display_name       = "allow-ports-3190-3199"
      action             = "ALLOW"
      direction          = "IN_OUT"
      ip_version         = "IPV4_IPV6"
      services           = [nsxt_policy_service.ports_3190_3199_service[0].path]
      source_groups      = ["10.74.85.2/32"]
      destination_groups = ["${var.k8s_lb_public_ip}"]
      scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
    }
  }

  dynamic "rule" {
    for_each = local.ports_3290_3299 ? [""] : []
    content {
      display_name       = "allow-ports-3290-3299"
      action             = "ALLOW"
      direction          = "IN_OUT"
      ip_version         = "IPV4_IPV6"
      services           = [nsxt_policy_service.ports_3290_3299_service[0].path]
      source_groups      = ["10.74.85.2/32"]
      destination_groups = ["${var.k8s_lb_public_ip}"]
      scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
    }
  }
"""


def file_filter(df):
    return (
        first_part()
        + ("").join(
            [
                f"""
  rule {{
    display_name       = "allow-{row["dest_port"]}-{row["source_ip"]}"
    action             = "{row["BLOCK/ALLOW"]}"
    direction          = "IN_OUT"
    ip_version         = "IPV4_IPV6"
    source_groups      = ["{row["source_ip"]}/{row["source_ip_range"]}"]
    destination_groups = ["${{var.k8s_lb_public_ip}}"]
    services           = [nsxt_policy_service.port_{row["dest_port"]}_service.path]
    scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
  }}
"""
                for index, row in df.iterrows()
            ]
        )
        + """

  rule {
    display_name       = "allow-12200-12201"
    action             = "ALLOW"
    direction          = "IN_OUT"
    ip_version         = "IPV4_IPV6"
    source_groups      = ["10.55.53.0/24", "10.55.54.0/24"]
    destination_groups = ["${var.k8s_lb_public_ip}"]
    services           = [nsxt_policy_service.port_12200_service.path, nsxt_policy_service.port_12201_service.path]
    scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
  }

  rule {
    display_name       = "allow-3408"
    action             = "ALLOW"
    direction          = "IN_OUT"
    ip_version         = "IPV4_IPV6"
    source_groups      = ["10.124.20.2/32"]
    destination_groups = ["${var.k8s_lb_public_ip}"]
    services           = [nsxt_policy_service.port_3408_service.path]
    scope              = [data.nsxt_policy_tier1_gateway.k8s_tier1_router.path]
  }

}

locals {
  standard_ports_tcp  = ["80", "443", "6443"]
  standard_ports_udp  = []
  ports_3190_3199_tcp = ["3190-3199"]
  ports_3206_3207_tcp = ["3206-3207"]
  ports_3290_3299_tcp = ["3290-3299"]

  standard_ports      = (length(local.standard_ports_tcp) > 0 || length(local.standard_ports_udp) > 0)
  ports_3190_3199     = (length(local.ports_3190_3199_tcp) > 0)
  ports_3206_3207     = (length(local.ports_3206_3207_tcp) > 0)
  ports_3290_3299     = (length(local.ports_3290_3299_tcp) > 0)
}

resource "nsxt_policy_service" "standard_ports_service" {
  count        = local.standard_ports ? 1 : 0
  display_name = "standard-ports-service"

  dynamic "l4_port_set_entry" {
    for_each = { for key, value in { TCP = local.standard_ports_tcp, UDP = local.standard_ports_udp } : key => value if length(value) > 0 }
    content {
      display_name      = "standard-ports"
      destination_ports = l4_port_set_entry.value
      protocol          = l4_port_set_entry.key
    }
  }

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }
}


resource "nsxt_policy_service" "ports_3190_3199_service" {
  count        = local.ports_3190_3199 ? 1 : 0
  display_name = "ports-3190_3199-service"

  dynamic "l4_port_set_entry" {
    for_each = { for key, value in { TCP = local.ports_3190_3199_tcp } : key => value if length(value) > 0 }
    content {
      display_name      = "ports_3190_3199"
      destination_ports = l4_port_set_entry.value
      protocol          = l4_port_set_entry.key
    }
  }

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }
}

resource "nsxt_policy_service" "ports_3206_3207_service" {
  count        = local.ports_3206_3207 ? 1 : 0
  display_name = "ports-3206_3207-service"

  dynamic "l4_port_set_entry" {
    for_each = { for key, value in { TCP = local.ports_3206_3207_tcp } : key => value if length(value) > 0 }
    content {
      display_name      = "ports_3206_3207"
      destination_ports = l4_port_set_entry.value
      protocol          = l4_port_set_entry.key
    }
  }

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }
}

resource "nsxt_policy_service" "ports_3290_3299_service" {
  count        = local.ports_3290_3299 ? 1 : 0
  display_name = "ports-3290_3299-service"

  dynamic "l4_port_set_entry" {
    for_each = { for key, value in { TCP = local.ports_3290_3299_tcp } : key => value if length(value) > 0 }
    content {
      display_name      = "ports_3290_3299"
      destination_ports = l4_port_set_entry.value
      protocol          = l4_port_set_entry.key
    }
  }

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }
}
"""
        + ("").join(
            [
                f"""
resource "nsxt_policy_service" "port_{row["dest_port"]}_service" {{
  display_name = "{row["dest_port"]}-port-service"
  l4_port_set_entry {{
    display_name      = "{row["dest_port"]}-port"
    protocol          = "{row["dest_port_type"]}"
    destination_ports = ["{row["dest_port"]}"]
  }}

  tag {{
    scope = var.env_name
    tag   = "gateway_policy"
  }}
}}
"""
                for index, row in df.iterrows()
            ]
        )
        + """

resource "nsxt_policy_service" "ssh_port_service" {
  display_name = "ssh-port-service"
  l4_port_set_entry {
    display_name      = "ssh-port"
    protocol          = "TCP"
    destination_ports = ["22"]
  }

  tag {
    scope = var.env_name
    tag   = "gateway_policy"
  }
}

####    Tier 1 Gateway

data "nsxt_policy_tier1_gateway" "k8s_tier1_router" {
  display_name = "${var.env_name}-dmz"
}
"""
    )
