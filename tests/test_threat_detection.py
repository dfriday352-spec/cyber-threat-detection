"""Tests for threat detection module"""

import pytest
from src.threat_detection.models import ThreatDetector


@pytest.fixture
def threat_detector():
    """Create threat detector instance"""
    config = {
        "thresholds": {"high_risk": 0.9, "medium_risk": 0.7, "low_risk": 0.5},
        "features": {"feature_count": 128}
    }
    return ThreatDetector(config)


def test_threat_detection_initialization(threat_detector):
    """Test threat detector initialization"""
    assert threat_detector is not None
    assert threat_detector.config is not None


def test_analyze_event(threat_detector):
    """Test event analysis"""
    event = {"source_ip": "192.168.1.1", "destination_ip": "10.0.0.1"}
    result = threat_detector.analyze_event(event)
    
    assert "is_threat" in result
    assert "combined_risk_score" in result
    assert 0 <= result["combined_risk_score"] <= 1
