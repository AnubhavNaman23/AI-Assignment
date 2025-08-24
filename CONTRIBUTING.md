# Contributing to LQT AI Assignment

Thank you for your interest in contributing to the LQT AI Assignment project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/LQT-AI-assignment.git
   cd LQT-AI-assignment
   ```

2. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Types of Contributions

We welcome various types of contributions:

- 🐛 **Bug fixes**
- ✨ **New features**
- 📖 **Documentation improvements**
- 🧪 **Tests**
- 🎨 **Code style improvements**
- 📊 **New algorithms or models**

## 📋 Development Guidelines

### Code Style

We follow PEP 8 for Python code style. Use these tools:

```bash
# Format code
black .

# Sort imports
isort .

# Check style
flake8 .
```

### Testing

- Write tests for new functionality
- Ensure all tests pass before submitting
- Aim for good test coverage

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Documentation

- Update docstrings for new functions/classes
- Add type hints where appropriate
- Update relevant documentation files

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add support for neural network models
fix: resolve data loading issue with CSV files
docs: update API documentation
test: add tests for classification models
```

## 🔄 Pull Request Process

1. **Update your branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run quality checks**
   ```bash
   black .
   isort .
   flake8 .
   pytest tests/
   ```

3. **Push your changes**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create pull request**
   - Provide clear description of changes
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

5. **Code review**
   - Address reviewer feedback
   - Update tests if needed
   - Ensure CI passes

## 🏗️ Project Structure

```
src/
├── data/           # Data loading and preprocessing
├── models/         # ML model implementations
├── features/       # Feature engineering
├── visualization/  # Plotting and visualization
└── utils/          # Utility functions

tests/              # Test files
notebooks/          # Jupyter notebooks
docs/               # Documentation
```

## 🎯 Coding Standards

### Python Code

```python
"""
Module docstring explaining purpose.
"""

from typing import Optional, List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ExampleClass:
    """
    Class docstring explaining purpose.
    
    Args:
        param1: Description of parameter
        param2: Description of parameter
    """
    
    def __init__(self, param1: str, param2: Optional[int] = None):
        self.param1 = param1
        self.param2 = param2
    
    def example_method(self, data: List[float]) -> Dict[str, Any]:
        """
        Method docstring explaining purpose.
        
        Args:
            data: Input data description
            
        Returns:
            Dictionary containing results
            
        Raises:
            ValueError: When data is invalid
        """
        if not data:
            raise ValueError("Data cannot be empty")
            
        result = {"processed": True, "count": len(data)}
        logger.info(f"Processed {len(data)} items")
        return result
```

### Jupyter Notebooks

- Clear markdown headers and explanations
- Well-commented code cells
- Remove output before committing
- Include summary/conclusions

## 🐛 Bug Reports

When reporting bugs, please include:

- **Environment**: Python version, OS, dependencies
- **Steps to reproduce**: Clear, minimal example
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Additional context**: Screenshots, logs, etc.

## 💡 Feature Requests

For new features, please provide:

- **Use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives**: Other approaches considered
- **Additional context**: Examples, mockups, etc.

## 📊 Adding New Models

When adding new ML models:

1. **Inherit from BaseMLModel**
   ```python
   from src.models.base import BaseMLModel
   
   class YourModel(BaseMLModel):
       def __init__(self, **kwargs):
           super().__init__("YourModelName")
           # Initialize your model
   ```

2. **Implement required methods**
   - `fit(X, y)`: Training logic
   - `predict(X)`: Prediction logic
   - `predict_proba(X)`: Probability predictions (if applicable)

3. **Add tests**
   ```python
   def test_your_model():
       model = YourModel()
       model.fit(X_train, y_train)
       predictions = model.predict(X_test)
       assert len(predictions) == len(X_test)
   ```

4. **Update documentation**
   - Add to README.md
   - Include in notebooks
   - Update API docs

## 🚀 Performance Guidelines

- Profile code for performance bottlenecks
- Use vectorized operations (NumPy/Pandas)
- Consider memory usage for large datasets
- Add timing benchmarks for new algorithms

## 📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

- Open an issue for technical questions
- Check existing issues for similar problems
- Reach out to maintainers for guidance

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special mentions for outstanding contributions

---

Thank you for contributing to the LQT AI Assignment project! 🎉
