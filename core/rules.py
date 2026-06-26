from abc import ABC, abstractmethod
import re

# 1. Primeiro define a classe base
class SecurityRule(ABC):
    @abstractmethod
    def run(self, lines):
        pass

# 2. Depois define as implementações que herdam de SecurityRule
class SQLInjectionRule(SecurityRule):
    """Detects SQL injection (CWE-89) with business context metadata."""
    def run(self, lines):
        violations = []
        pattern = r"f[\"']\s*SELECT.*?(FROM|WHERE|INSERT|UPDATE)"
        for idx, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                violations.append({
                    "rule_id": "V-SEC-001",
                    "severity": "CRITICAL",
                    "description": "Direct SQL query concatenation using f-strings.",
                    "business_impact": "High: Risk of SQL Injection.",
                    "remediation_effort": "2h",
                    "line": idx + 1,
                    "cwe": "CWE-89",
                    "cvss": "9.1",
                    "asset": "Auth-Module"
                })
        return violations

class HardcodedSecretRule(SecurityRule):
    """Detects hardcoded secrets (CWE-798) with remediation guidance."""
    def run(self, lines):
        violations = []
        pattern = r"(password|secret|key|token)\s*=\s*['\"][\w!@#$%^&*()]{8,}['\"]"
        for idx, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                violations.append({
                    "rule_id": "V-SEC-002",
                    "severity": "CRITICAL",
                    "description": "Hardcoded credentials detected.",
                    "business_impact": "Critical: System compromise.",
                    "remediation_effort": "1h",
                    "line": idx + 1,
                    "cwe": "CWE-798",
                    "cvss": "9.8",
                    "asset": "DB-Connector"
                })
        return violations