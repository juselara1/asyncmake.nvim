{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-23.05";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
    in rec {
      devShell = pkgs.mkShell {
        LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
        buildInputs = with pkgs; [
          python311 python311Packages.pip git git-lfs
        ];
      };
    }
  );
}
