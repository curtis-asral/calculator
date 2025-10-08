import os
import pandas as pd
import pytest
import tempfile
from app.memento import history, undo, redo, clear_history


@pytest.fixture
def setup_history(monkeypatch):
    """Create temp CSV and set env var for history."""
    tmp = tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False)
    pd.DataFrame({"equation": ["1+1 = 2", "2+2 = 4", "3+3 = 6"]}).to_csv(tmp.name, index=False)
    monkeypatch.setenv("history", tmp.name)
    yield tmp.name
    os.remove(tmp.name)


def test_undo_and_redo(setup_history):
    undone = undo()
    assert undone == "3+3 = 6"

    redone = redo()
    assert redone == "3+3 = 6"

    df = pd.read_csv(setup_history)
    assert "3+3 = 6" in df["equation"].tolist()


def test_history_and_clear_history(setup_history):
    # Check initial history matches CSV
    assert history() == ["1+1 = 2", "2+2 = 4", "3+3 = 6"]

    # Clear and confirm empty
    clear_history()
    try:
        df = pd.read_csv(setup_history)
    except:
        df = pd.DataFrame(columns=["equation"])
    assert df.empty


def test_undo_and_redo_when_empty(monkeypatch, tmp_path):
    # Create empty history CSV
    path = tmp_path / "empty.csv"
    pd.DataFrame(columns=["equation"]).to_csv(path, index=False)
    monkeypatch.setenv("history", str(path))

    assert undo() is None
    assert redo() is None
