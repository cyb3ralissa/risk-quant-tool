class RiskScenario:
    def __init__(self, name, likelihood, impact, mitigation_cost):
        self.name = name
        self.likelihood = likelihood  # Probability between 0 and 1
        self.impact = impact          # Monetary impact
        self.mitigation_cost = mitigation_cost  # Cost to mitigate the risk

    def expected_loss(self):
        """Calculate expected loss as likelihood * impact"""
        return self.likelihood * self.impact

    def summary(self):
        """Return a summary of the risk scenario"""
        return (
            f"Risk Scenario: {self.name}\n"
            f"Likelihood: {self.likelihood}\n"
            f"Impact: ${self.impact:,.2f}\n"
            f"Mitigation Cost: ${self.mitigation_cost:,.2f}\n"
            f"Expected Loss: ${self.expected_loss():,.2f}"
        )
