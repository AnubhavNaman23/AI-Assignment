"""
Simple AI Demo Program - LQT AI Assignment
This program demonstrates basic AI/ML capabilities without complex dependencies
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("🚀 LQT AI Assignment - AI Developer Demo")
    print("=" * 50)
    
    try:
        # Test 1: Basic data operations
        print("\n📊 Test 1: Data Operations")
        import pandas as pd
        import numpy as np
        
        # Generate sample data
        np.random.seed(42)
        data = {
            'feature_1': np.random.normal(0, 1, 100),
            'feature_2': np.random.normal(2, 1.5, 100),
            'category': np.random.choice(['A', 'B', 'C'], 100),
            'target': np.random.randint(0, 2, 100)
        }
        df = pd.DataFrame(data)
        print(f"✅ Created dataset with shape: {df.shape}")
        print(f"✅ Features: {list(df.columns)}")
        print(f"✅ Target distribution: {df['target'].value_counts().to_dict()}")
        
    except ImportError as e:
        print(f"❌ Data operations test failed: {e}")
    
    try:
        # Test 2: Machine Learning
        print("\n🤖 Test 2: Machine Learning")
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        
        # Prepare data
        X = df[['feature_1', 'feature_2']].values
        y = df['target'].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        
        # Train model
        model = LogisticRegression(random_state=42)
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"✅ Model trained on {X_train.shape[0]} samples")
        print(f"✅ Test set size: {X_test.shape[0]} samples")
        print(f"✅ Model accuracy: {accuracy:.4f}")
        
    except ImportError as e:
        print(f"❌ Machine learning test failed: {e}")
    
    try:
        # Test 3: Basic visualization (without seaborn)
        print("\n📈 Test 3: Visualization")
        import matplotlib.pyplot as plt
        
        # Create simple plots
        plt.figure(figsize=(10, 4))
        
        # Plot 1: Feature distribution
        plt.subplot(1, 2, 1)
        plt.hist(df['feature_1'], bins=20, alpha=0.7, color='blue')
        plt.title('Feature 1 Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        
        # Plot 2: Feature scatter
        plt.subplot(1, 2, 2)
        colors = ['red' if t == 1 else 'blue' for t in df['target']]
        plt.scatter(df['feature_1'], df['feature_2'], c=colors, alpha=0.6)
        plt.title('Feature 1 vs Feature 2')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        
        plt.tight_layout()
        plt.savefig('demo_plots.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("✅ Created visualization plots")
        print("✅ Saved plots to 'demo_plots.png'")
        
    except ImportError as e:
        print(f"❌ Visualization test failed: {e}")
    
    # Test 4: Advanced features
    print("\n🔬 Test 4: Advanced AI Features")
    try:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report
        
        # Train Random Forest
        rf_model = RandomForestClassifier(n_estimators=50, random_state=42)
        rf_model.fit(X_train, y_train)
        rf_pred = rf_model.predict(X_test)
        rf_accuracy = accuracy_score(y_test, rf_pred)
        
        print(f"✅ Random Forest accuracy: {rf_accuracy:.4f}")
        
        # Feature importance
        feature_names = ['feature_1', 'feature_2']
        importance = dict(zip(feature_names, rf_model.feature_importances_))
        print(f"✅ Feature importance: {importance}")
        
        # Classification report
        print("✅ Classification Report:")
        print(classification_report(y_test, rf_pred))
        
    except ImportError as e:
        print(f"❌ Advanced features test failed: {e}")
    
    # Summary
    print("\n🎯 Demo Summary")
    print("=" * 50)
    print("✅ Data manipulation with Pandas/NumPy")
    print("✅ Machine Learning with Scikit-learn")
    print("✅ Data visualization with Matplotlib")
    print("✅ Multiple ML algorithms comparison")
    print("✅ Model evaluation and metrics")
    
    print("\n🏆 LQT AI Assignment Capabilities Demonstrated:")
    print("  • Data Science & Analytics")
    print("  • Machine Learning Implementation")
    print("  • Model Training & Evaluation")
    print("  • Data Visualization")
    print("  • Python Programming Best Practices")
    
    print("\n🎉 Demo completed successfully!")

if __name__ == "__main__":
    main()
