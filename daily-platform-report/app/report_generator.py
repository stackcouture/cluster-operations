def generate(summary):

    report = f"""
==================================================
Daily Platform Report
==================================================

Date        : {summary.date}
Cluster     : {summary.cluster_name}
Environment : {summary.environment}

--------------------------------------------------
Cluster Health
--------------------------------------------------

Nodes Ready         : {summary.ready_nodes}/{summary.total_nodes}
Namespaces          : {summary.namespaces}
Running Pods        : {summary.running_pods}
Pending Pods        : {summary.pending_pods}
Failed Pods         : {summary.failed_pods}
CrashLoopBackOff    : {summary.crashloop_pods}

Overall Status      : {"Healthy" if summary.cluster_healthy else "Unhealthy"}

--------------------------------------------------
Workload Status
--------------------------------------------------

Deployments Healthy : {summary.ready_deployments}/{summary.total_deployments}
StatefulSets Ready  : {summary.ready_statefulsets}/{summary.total_statefulsets}
DaemonSets Ready    : {summary.ready_daemonsets}/{summary.total_daemonsets}
"""

    return report